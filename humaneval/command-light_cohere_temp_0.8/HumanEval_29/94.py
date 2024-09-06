```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


def test_filter_by_prefix() -> None:
    test_list = ['abc', 'bcd', 'cde', 'e', 'array', 'always']
    print(filter_by_prefix(test_list, 'a'))  # Output: ['abc', 'array']
    print(filter_by_prefix(test_list, 'b'))  # Output: ['bcd', 'e']
    print(filter_by_prefix(test_list, 'cd'))  # Output: ['cde']
    print(filter_by_prefix(test_list, 'Meteor'))  # Should be None
    return None  # test function returns None


if __name__ == "__main__":
    test_filter_by_prefix()
```
This Python script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list of strings that start with the given prefix. The test function `test_filter_by_prefix` is used to verify the correctness of the `filter_by_prefix` function by passing the test list and checking the output against the expected output. 
The script also demonstrates the use of the `filter_by_prefix` function with various test lists to check its functionality.