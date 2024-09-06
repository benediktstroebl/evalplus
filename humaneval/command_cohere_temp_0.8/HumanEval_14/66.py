```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: x != '', string))));
```
The function utilizes the `dropwhile` function from the `itertools` module to eliminate elements from the start of the string up until it reaches an empty string. The `reversed` function is then used to arrange the list of prefixes in descending order - from the longest to the shortest.

To validate the correctness of the implemented function, test cases are executed to check for the following:
- **Behavior for Empty String**: The function should yield an empty list when an empty string is provided.
- **Behavior for Single Character**: The function should produce a list containing only the character when a string with a single character is provided.
- **Behavior for Regular String**: The function should produce a list containing all prefixes in the expected order for a regular string.

Here is an example demonstrating how to execute the test cases:
```python
def test_all_prefixes_function():
    # Test Case 1: Empty String
    assert all_prefixes('') == []

    # Test Case 2: Single Character
    assert all_prefixes('a') == ['a']

    # Test Case 3: Regular String
    assert all_prefixes('abc') == ['a', 'ab', 'abc']

test_all_prefixes_function()
```
Each test case demonstrates a specific scenario the function should handle, ensuring its adaptability across various scenarios.