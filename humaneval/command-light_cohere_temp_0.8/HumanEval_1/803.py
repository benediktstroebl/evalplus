Here is a self-contained Python script that solves the problem of separating and identifying parenthesis groups:
```python
def separate_paren_groups(s: str) -> List[str]:
    return ['(' + c + ')', ')' + c for c in s.group() if c != ' ')
```

This script defines a function named `separate_paren_groups` that takes a string `s` as input and returns a list of separated parenthesis groups. It utilizes a unique approach by creating new strings by concatenating the current content `c` with an opening parenthesis `(`),` and adding a closing parenthesis `)`. The function also ignores any space characters. 

This code is self-contained and does not require any external modules or functions.