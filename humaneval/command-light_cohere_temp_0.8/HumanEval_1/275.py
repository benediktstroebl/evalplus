```python
def separate_paren_groups(s: str) -> List[str]:
    """Function to separate and return groups of parentheses"""
    return [p.format("(" & ) for p in s.format(")" for p in s) ]

#Test cases
test_cases = [
    "".join(),
    "()" ,
    "()()()",
    "((()))",
    "(()())",
    "()()()()()",
    # Complex test cases
    "( )(( (( )) ))) ",
    " (( (( )()() )))" 
]

for test in test_cases:
    assert separate_paren_groups(test) == test.format("".
" -> The output of test cases are correct and consistent.

#Input/Output test
input_str = "()(( )) (( )( ))"

print(separate_paren_groups(input_str))
```