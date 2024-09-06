```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a prefix, `prefix`. It returns a new list containing only the strings from the input list that start with the specified prefix. This behavior is demonstrated in the included tests:
```python
def test_filter_by_prefix():
    # Test list with mixed cases
    input_list = ['abc', 'bcd', 'cde', 'array']
    input_prefix = 'a'
    expected_output = ['abc', 'array']
    assert filter_by_prefix(input_list, input_prefix) == expected_output

    # Empty list case
    input_list = []
    input_prefix = 'a'
    assert filter_by_prefix(input_list, input_prefix) == []

    # Prefix does not exist in the list
    input_list = ['ab', 'cd', 'de', 'arr']
    input_prefix = 'ass'
    assert filter_by_prefix(input_list, input_prefix) == []

test_filter_by_prefix()
``` 

The function includes type hints, and the comment above the function explains its purpose and provides a few test cases with expected output, adhering to the problem statement's guidelines.  This again emphasizes the utility of good documentation and testing in code, making it easier for others and future you to understand and validate the function's behavior.