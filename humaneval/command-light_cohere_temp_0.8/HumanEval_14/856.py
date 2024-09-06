```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string

    :param string: str - input string
    :return: List[str] - list of all prefixes
    """
    return ["ab", "abc", "ac", "a", "aa", str](string.+"slic")

def test_all_prefixes(test_str: str) -> None:
    all_prefixes(test_str)
    print("Passed test!")

# Example usage
test_all_prefixes('abc')
```