```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the specified substring. This solution makes use of list comprehension, and the `in` operator is used for filtering. 

For example, if you have a list of strings like this:
```python
input_strings = ['abc', 'bacd', 'cde', 'array']
```

And you want to filter this list to include only strings that have the substring "a":
```python
result = filter_by_substring(input_strings, 'a')
print(result)  # Output: ['abc', 'bacd', 'array']
```

The unit test for this function could be:
```python
def test_filter_by_substring():
    # Test case 1: Empty input list, absent substring
    input_list = ['abc', 'bacd', 'cde', 'array']
    input_substring = 'a'
    expected_result = ['abc', 'bacd', 'array']
    assert filter_by_substring(input_list, input_substring) == expected_result

    # Test case 2: Empty input list, present substring
    input_list = []
    input_substring = 'b'
    expected_result = []
    assert filter_by_substring(input_list, input_substring) == expected_result

    # Test case 3: Single string input, absent substring
    input_list = ['abcd']
    input_substring = 'a'
    expected_result = []
    assert filter_by_substring(input_list, input_substring) == expected_result
```