from typing import *
from dataclasses import dataclass
import sys

@dataclass
class TuringMachine:
    alphabet: str
    tape: List[str]
    head_position: int
    current_state: str
    accepting_states: List[str]
    rules: List[str]

    def print_current_tape(self):
        '''Prints the current tape state at any given time'''
        tape_str: str = ''
        blank_space: str = ''

        # introduce blank space to align head with its position
        if self.head_position > 0:
            for i in range(self.head_position):
                blank_space += '    '

        # create formatted and aligned tape string
        for i, j in enumerate(self.tape):
            if i == 0:
                tape_str += self.tape[i]
            else:
                tape_str += f' | {self.tape[i]}'

        head: str = blank_space + '^'

        return f'{tape_str}\n{head}'

    def read_cell(self) -> str:
        return self.tape[self.head_position]

    def write_cell(self, write_value: str):
        if len(write_value) == 1:
            self.tape[self.head_position] = write_value
        else:
            raise Exception('Attempted to write a value of length not equal to 1. Aborting...')

    def move_head(self, direction: str):
        match direction:
            case 'l':
                self.head_position -= 1

                if self.head_position < 0:
                    self.tape.insert(0, '.')
                    self.head_position = 0

            case 'r':
                self.head_position += 1

                if self.head_position >= len(self.tape):
                    self.tape.append('.')
                    self.head_position = len(self.tape) - 1

    def switch_state(self, state: str):
        self.current_state = state
    
    def run(self):
        # validates cell value
        if self.read_cell() not in self.alphabet:
            raise Exception('A value in the tape is not in the machine\'s alphabet. Consider changing the alphabet to include all values used in the tape.')
        
        print(self.print_current_tape())
        
        while True:
            for i in self.rules:
                cell: str = self.read_cell()
                if i[0] == self.current_state and cell in i[1]: # runs if rule matches current criteria
                    if i[2] != 'none':
                        self.write_cell(i[2])

                    self.move_head(i[3])
                    self.switch_state(i[4])

                    print(self.print_current_tape())
                    break
                
            else: # no valid rules remaining
                if self.current_state in self.accepting_states:
                    return 'Accepted'
                return 'Rejected'

def validate_identifier(s: str) -> bool:
    '''Checks that a given machine attribute identifier is an identifier and not an identifier argument'''
    for i in s:
        if not i.isalnum() and i != '_':
            return False

    return True


def read_machine(file: str) -> List[str]:
    '''Read init data from given turing machine file (filename.tm)'''
    with open(file, 'r') as f:
        lines: List[str] = f.read().split('\n')

    processed: List[str] = []

    for line in lines:
        parts: List[str] = line.split(': ', 1)
        if len(parts) > 1 and validate_identifier(parts[0]):
            processed.append(parts)

    return processed

def parse(data):
    '''Parse the processed data from the read_machine function'''
    alphabet, tape, head_position, current_state, accepting_states, rules = '', [], 0, '', [], []

    for i, j in data:
        match i:
            case 'alphabet':
                alphabet += j

            case 'tape':
                for c in j:
                    tape.append(c)

            case 'tape_offset':
                head_position += int(j)

            case 'start_state':
                current_state += j

            case 'accepting_states':
                states: List[str] = j.split(' ')
                for state in states:
                    accepting_states.append(state)

            case 'rule':
                rules.append(j.split(' '))

    return alphabet, tape, head_position, current_state, accepting_states, rules

# for CLI usage, see https://github.com/jadedevs/TuringMachineInterpreter README.md. if you want to use this without a CLI, paste your machine path in place of str(sys.argv[1])
tm = TuringMachine(*parse(read_machine(sys.argv[1])))

print(tm.run())
