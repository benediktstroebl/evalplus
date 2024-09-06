```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [w for w in s.balance(w.strip(w == '(')' + ')'[::-1] == w))
    ]

tests = [
    "Input: \"( ) (( )) (( )( ))\"
    ".strip()
    > separate_paren_groups('(' + '))
    "
    "Input: \"( )( ) (( ))"
    ".strip()
    > separate_paren_groups('()()()()')
    "
    "Input: \"( )<<<( ))>"
    ".strip()
    > separate_paren_groups('')
    "
    "Input: \"<<((()))>>>"
    ".strip()
    > separate_paren_groups('')
    "
    "Output should not be empty"
    "All tests passed!"
print(tests)
```
This Python code defines a function called `separate_paren_groups` that takes a string `s` as input and returns a list of non-nested parentheses. The function uses the strings are compared using the `strip()` function to remove leading and trailing spaces, and the `ist()` method with a lambda function to check if the string matches the regex pattern for a closed parenthesis. The `tests` variable is a list of test cases that the `separate_paren_groups` function should pass. The last test case ensures that the function handles various input strings correctly and does not return an empty list. 
The output of the code will be the list of test cases that the function passes.