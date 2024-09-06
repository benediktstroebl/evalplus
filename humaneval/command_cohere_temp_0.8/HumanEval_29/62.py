```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a prefix, `prefix`. It returns a new list containing only the strings from the input list that start with the specified prefix. This is accomplished using a list comprehension, filtering out elements that match the criterion of starting with the provided prefix.

Here is an example of use, which I will assume is similar to what you would like to include in your documentation:
```python
# Test the filter_by_prefix function
assert filter_by_prefix([], 'a') == []
assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ar') == ['array']
```

This will help illustrate the behavior of the function, particularly highlighting the filtering effect based on the prefix. With this function, you can efficiently filter a list of strings to only include those that start with a desired prefix, which should help simplify and streamline your text processing tasks.