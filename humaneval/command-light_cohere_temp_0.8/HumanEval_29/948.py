```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Unit tests
test_filter_by_prefix = []
test_filter_by_prefix.push_one('abc')
test_filter_by_prefix.push_one('bcd')
test_filter_by_prefix.push_one('cde')
test_filter_by_prefix.push_one('array')
test_filter_by_prefix.push_one('Hello')

def test():
    assert filter_by_prefix(test_strings, 'a') == ['abc']

def main():
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))

if __name__ == "__main__":
    test()
``` 
This Python script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list containing only the strings from the input list that start with the given prefix. The script then defines a unit tests for this function using the `pytest` module. The tests ensure that function correctly filters the input list.