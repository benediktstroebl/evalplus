```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates groups of opening parentheses ( ) ) from the rest of the string.
    Parameters:
    s (str) - Input string containing potential groups of opening parentheses

    Returns:
    List[str] - List of separated opening parentheses
    """
    brackets = []
    while ')' in s:
        if '(' in s[:s.find(')')] + 1:
            brackets.append(')')
       
        s = s.find(')'). Plus 1) = s = ''
    s = ' ' + s
    return brackets

# Test cases
tests = [
    '() () (( ))',
    '( )()()()',
    '()  ( )',
    '(())'
]

for case in tests:
    actual_result = separate_paren_groups(case)
    print(case, '->', ', '.join(actual_result))
```
The provided Python script defines a function `separate_paren_groups` that takes a string as input and aims to separate groups of opening parentheses from the rest of the string.

The function uses a loop to iterate over each character in the string. Inside the loop, it checks if the character is ')' and if there is a corresponding '(' somewhere before the ')' (indicating the position of the ')' with a +1 offset) to find the last closing parenthesis.

If a ')' is found, it appends it to the `brackets` list, and the string is updated to skip the ')' and any characters after it. After the loop ends, the string contains only spaces, and the function returns the `brackets` list, which contains all the separated opening parentheses. 

The script then defines a set of test cases, and loops over them, passing each case to the `separate_paren_groups` function. The function prints out the the expected output next to each test case.