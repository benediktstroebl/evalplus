```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        nest = 0
        for c in chunk:
            if c == '(':
                nest += 1
            else:
                nest -= 1
        result.append(nest)
    return result
```
The `parse_nested_parens` function takes a string as input and splits it into chunks based on spaces. It keeps a `nest` variable to track the current nesting level, increments it for every opening parenthesis `(`, and decrements it for every closing parenthesis `)`. The resulting list of nesting levels is returned.

To test this, you can run the following code to check if the output is as expected:
```python
test_strings = ['(()()) ((())) () ((())()())', '((()))', '(()())', '()', '((a))', '(a)', 'a']
expected_results = [2, 3, 2, 1, 1, 0]
for string, result in zip(test_strings, expected_results):
    print(f"Input: {string}")
    print(f"Output: {parse_nested_parens(string)}")
    print(f"Expected: {result}\n")
```
This will show the results of running the provided code on each test case and comparing the output against the expected result.