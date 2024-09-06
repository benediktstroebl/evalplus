```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the specified substring. It uses a list comprehension, iterating over each string in `strings`, and adding those that contain `substring` to the new list.

The behaviour of the function is well-defined even if an empty substring is provided, or if `substring` is present in all or none of the strings in the input list. In these cases, the function will return the entirety of `strings` or an empty list, respectively. 

The unit tests provided are straightforward and effective in verifying the function's correctness:
```python
def test_filter_by_substring():
    # Empty input
    assert filter_by_substring([], 'a') == []

    # Single string
    assert filter_by_substring(['abc'], 'a') == ['abc']

    # Multiple strings, one containing substring
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

    # Multiple strings, none containing substring
    assert filter_by_substring(['abc', 'bcd', 'cde', 'arr'], 'xyz') == []

    # Multiple strings, all containing substring
    assert filter_by_substring(['abc', 'bacd', 'cdea', 'array'], 'a') == ['abc', 'bacd', 'cdea', 'array']

test_filter_by_substring()
```

These tests cover a variety of scenarios, including empty input, single-element input, partial matches, and complete matches, ensuring that the function's behavior is correct in all cases.  If there are additional requirements or specific edge cases to handle, further testing and function adjustments might be necessary.