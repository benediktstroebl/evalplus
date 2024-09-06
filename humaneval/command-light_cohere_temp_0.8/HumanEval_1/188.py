Here is a self-contained Python script that solves the problem of separating parentheses into groups:
```python
def separate_paren_groups(s):
    return ['(' + e + ')' for e in s.group() if e != '('] + ['('] + [')')]

# Test cases
test_cases = [
    '()',
    '(())',
    '(()())',
    '( ) (( ))',
    '(((((()))))))',
    '((()()())())'
]

for test_case in test_cases:
    if separate_paren_groups(test_case) != test_case:
        print(f"ERROR: {test_case} is not correct.")
```

This script defines a function called `separate_paren_groups` that takes a string of parentheses (`') as input and returns a list of separated groups. It also has a test cases to check the correctness of the function.