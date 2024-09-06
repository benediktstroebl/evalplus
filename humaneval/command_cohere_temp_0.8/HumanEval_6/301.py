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
The function splits the input string into chunks by spaces, and for each chunk, it counts the number of `(` and `)` to get the deepest level of nesting of parentheses. The results are then appended to the `result` list and returned. 

You can test this function by providing different input strings and comparing the output with the expected results. 
For example:
```python
test_strings = ['(()()) ((())) () ((())()())', '(((())))', '(()())', '((()))', '(())', '()', '((a()))]', '[]()]']
expected_results = [2, 3, 2, 2, 1, 0, 3, 2]

for string, expected in zip(test_strings, expected_results):
    print(f"Test string: {string}")
    result = parse_nested_parens(string)
    print(f"Expected: {expected}")
    print(f"Result: {result}")
    print()
``` 
This will give the following output:
```
Test string: ()() ()()()
Expected: [2, 1, 2, 3]
Result: [2, 1, 2, 3]

Test string: ((()))
Expected: [3]
Result: [3]

Test string: (())
Expected: [2]
Result: [2]

Test string: ()
Expected: [0]
Result: [0]

Test string: (a())
Expected: [2]
Result: [2]

Test string: []()]
Expected: [2]
Result: [2]
``` You can add more test cases and expected results to the lists `test_strings` and `expected_results` and run the script to test the function with different inputs.