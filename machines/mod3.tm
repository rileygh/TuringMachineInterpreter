Machine Syntax is defined in the README file at https://github.com/rileygh/TuringMachineInterpreter

Example machine that accepts input divisible by 3
alphabet: 0123456789
tape: 14256
tape_offset: 0
start_state: S0
accepting_states: S0
rule: S0 0369 none r S0
rule: S0 147 none r S1
rule: S0 258 none r S2
rule: S1 0369 none r S1
rule: S1 147 none r S2
rule: S1 258 none r S0
rule: S2 0369 none r S2
rule: S2 147 none r S0
rule: S2 258 none r S1
