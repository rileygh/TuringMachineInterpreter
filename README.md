# Turing Machine Interpreter
A basic interpreter for Turing Machines.

### It is strongly advised to have some knowledge of the operations of a [Turing Machine](https://en.wikipedia.org/wiki/Turing_machine) before using this program.

---

## Usage
### CLI Arguments
```
usage: python -m interpreter [machine file path]
```

---

## Creating Turing Machine (.tm) files
The Turing Machine files used by this program follow a basic syntax, which is explained below:

```
This file does nothing, running it will not give you any meaningful results. It is solely an example.
alphabet: xyz
tape: xxyyzz
tape_offset: 0
start_state: S0
accepting_states: S0 S1
rule: S0 xy yz r S1
```

The `alphabet` keyword defines the set of characters that can be placed in a cell on the tape. Give every character contained in the alphabet consecutively in a string.

The `tape` keyword defines the initial values written on the tape.

The `tape_offset` keyword refers to the rightward offset of the head upon initialising the tape. Set this to any integer n where n is in the range 0 to the length of the initial tape.

The `start_state` keyword defines the state in which the program will begin in.

The `accepting_states` keyword defines the states which the program will accept as valid once the machine has finished running.

Multiple `rules` can be introduced. A rule will tell the program what to do when reading a certain value in a certain state. Rules can be defined using this syntax:
```
rule: <active state> <read value> <write value> <head movement direction> <next state>
```
Please note that you can set the write value to `none` if you do not want it to write anything to the cell.
