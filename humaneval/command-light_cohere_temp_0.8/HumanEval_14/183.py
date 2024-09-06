```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): Input string

    Returns:
        List[str]: List of all prefixes
    """
    return ['a' if i < string.find(i, 'a') else i for i in range(len(string))]
```