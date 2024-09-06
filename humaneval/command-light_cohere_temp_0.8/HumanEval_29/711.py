```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


def test_filter_by_prefix():
    strings = ['abc', 'bcd', 'cde', 'array', 'hello']
    prefix = 'a'

    result = filter_by_prefix(strings, prefix)
    assert result == ['abc', 'array'], "Failed test: Expected ['abc', 'array'], got %s"
    return result

# Run the tests
print(test_filter_by_prefix())
```  This code provides a filter_by_prefix function that takes a list of strings and a prefix as input and returns a new list that includes only the strings from the input list that start with the given prefix. 
The test_filter_by_prefix function tests the filter_by_prefix function by passing the test input and checking that the output is correct.   The print function then the test result, this will print out the test output to the console.