```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


def test_filter_by_prefix() -> None:
    test_list = ['abc', 'bcd', 'cde', 'array', 'hello']
    expected = ['abc', 'array']
    actual = filter_by_prefix(test_list, 'a')
    assert actual == expected, "filter_by_prefix did not return expected results"


# Run the test function to check the filter_by_prefix function
``` 
This code defines a function called `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list that contains only the strings that start with the given prefix. It is then uses the string `startswith` method to filter out the strings that do not start with the given prefix.