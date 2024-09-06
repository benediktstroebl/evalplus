```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Unit tests
strings = ["abc", "bacd", "cde", "array", "word", "wor"]
substrings = ["a", "aba", "bard", "text"]

test_strings = [strings] + [filter_by_substring(strings, substrings) for substrings in substrings]

test_cases = {
    "basic": test_strings[:2] + [strings[-1]]
    , 
    "all": test_strings + [filter_by_substring(test_strings, "x") for x in substrings]
    , 
    "non-existent": [filter_by_substring(strings, "z")]
}

def test_filter_by_substring():
    """ Function to run unit tests for filter_by_substring function """
    for test_case in test_cases:
        assert len(filter_by_substring(test_case, "")) == 0
        assert len(filter_by_substring(test_case, "a")) == 3
        assert len(filter_by_substring(test_case, "bard")) == 1
        assert len(filter_by_substring(test_case, "text")) == 1
        assert len(filter_by_substring(test_case, "aba")) == 2

if __name__ == "__main__":
    test_filter_by_substring()
``` 
The provided Python script defines a function `filter_by_substring` that filters a list of strings for instances containing a given substring. It also includes unit tests for the strings and the `filter_by_substring` function, testing various scenarios, including basic strings, filtering for specific substrings, and filtering for non-existent substrings.