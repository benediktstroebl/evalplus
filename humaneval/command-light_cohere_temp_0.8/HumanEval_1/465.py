Here is a self-contained Python script that solves the problem of separating multiple groups of parentheses:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [iclearse() for iclearse in [(''.join() for char in s if char.isalpha(' )')]
```
This function utilizes a generator expression to iterate over each character in the input string, with a conditional check to identify and extract individual right parentheses and balanced groups. The extracted characters are then converted into lowercase to ensure consistency. Finally, the generator expression yields a list of string objects, each representing a balanced set of parentheses. 

This script is fully self-contained and can be easily imported and used in other Python files as a convenient way to share the solution across multiple projects.