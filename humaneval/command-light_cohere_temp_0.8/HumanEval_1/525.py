Here's the self-contained Python function that solves the problem of separating parentheses into groups:
```python
def separate_paren_groups(s):
    return [ parse(ch) for ch in s ]


def parse(c):
    if c == '(': return '('  # same as (
    elif c == ')': return ')'  # same as )
    elif c == ' ': return ' '  # same as space
    else:
        return c  # non-balanced


# Testing
test_cases = [
    "()",           # single char
    "((()))",       # unbalanced
    "(())",       # balanced
    "(((((())))))",  # too much nesting
    "((()())())())",  # another balanced one
]

for case in test_cases:
    assert separate_paren_groups(case) == ['(', ')', ' ', '()', ']'], case
```

This function takes a string `s` as input and should return a list of strings, each representing a group of parentheses separated. The function uses a nested list comprehension to iterate over each character in the input string. The function uses a simple cases to determine the correct output, and asserts that the output is as expected.