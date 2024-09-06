```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]


# Test the function with a sample input
test_cases = [
    [],
    ['abc', 'a'],
    ['abc', 'a', 'array'],
    ['abc', 'bed'],
    ['abc'],
    ['abcd', 'a'],
    ['cde', 'a'],
    ['array', 'a'],
]

for case in test_cases:
    actual = filter_by_substring(case, 'a')
    assert actual == ['abc', 'array']
```  This Python code defines a function called `filter_by_substring` that filters a list of strings for instances that contain a specific substring. The function takes two inputs: a list of strings and a substring. It uses a `find()` method to search for the substring in each string and returns the strings that contain the substring. 

The code also provides a set of test cases to validate the function's behavior. The test cases include various combinations of strings and substring values. The code then iterates over the test cases and calls the `filter_by_substring` function with the `test_cases` list and the `substring` value 'a'. 

The `assert` statement is used to check if the actual output matches the expected output for each test case. 
If the actual output matches the expected output, the code passes the test and the assertion statement is True.