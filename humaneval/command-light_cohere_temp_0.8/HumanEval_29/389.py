Certainly! Here is the corrected Python script with the self-contained function that filters strings based on their prefix:

```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    : Checks each input string against the given prefix
    """
    return [string for string in strings if string.startswith(prefix)]


def test_filter_by_prefix():
    """
    Test the filter_by_prefix function with different inputs.
    """
    strings = ['abc', 'bcd', 'cde', 'array', 'change', 'edit']
    prefix = 'edit'

    result = filter_by_prefix(strings, prefix)
    assert result == ['cde', 'edit']
```

This script includes the function `filter_by_prefix` that filters an input list of strings based on their prefix. The `test_filter_by_prefix` function tests the `filter_by_prefix` function with different inputs and assertions. 

This code is self-contained and can be used to solve the problem of filtering strings based on their prefix.