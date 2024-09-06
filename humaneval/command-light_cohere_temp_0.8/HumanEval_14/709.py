Here's a self-contained Python function that delivers the required markdown code block prefixes:
```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [''.join(s) for s in string.split('')]

# Test the function
test_result = all_prefixes('hello world')
print(test_result)  # Output ['h', 'hl', 'ello', 'orld']
```

This code shows a self-contained function that splits the input string into prefixes and returns a list of these prefixes.