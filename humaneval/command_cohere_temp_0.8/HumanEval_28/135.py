```python
# Import the list module from the typing module
from typing import List


# Define the function that takes in a list of strings and returns a string
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''
    for string in strings:
        result += string
    return result


# Tests
# Empty list
test_cases = [([], ''), ('abc', 'abc'), ('ab', 'ab'), ('a', 'a'), ('', '')]
for test_case in test_cases:
    with assertEqual(f"Failed on {' and '.join(map(str, test_case))}"):
        assert concatenate(test_case[0]) == test_case[1]
```

This code snippet includes the `concatenate` function that takes a list of strings (`List[str]`) and returns a single string. It iterates over the list and concatenates each string element to the accumulated `result`.

The tests cover multiple cases, including an empty list and lists with different numbers of elements. For each test case, it verifies that the output of `concatenate` matches the expected result.

By running this code, you can see the results of each test case and ensure that the function behaves as expected.