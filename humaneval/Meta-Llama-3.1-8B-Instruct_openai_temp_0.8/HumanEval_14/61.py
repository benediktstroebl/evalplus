```python
from typing import List
from itertools import chain, combinations

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
    string (str): Input string

    Returns:
    List[str]: List of all prefixes in order from shortest to longest

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Generate all possible prefixes using itertools.chain and itertools.combinations
    # We use chain to combine the start and end indices of the range with a slice
    # We use combinations to generate the indices of the string
    all_prefixes = list(chain(*[string[:i+1] for i in range(len(string))]))
    # Return the list of prefixes sorted by length
    return sorted(all_prefixes, key=len)
```

In this script, we use `itertools.chain` and `itertools.combinations` to generate all possible prefixes of the input string. `itertools.chain` is used to combine the prefixes, and `itertools.combinations` is used to generate the indices of the string. The list of prefixes is then sorted by length and returned. 

Note that the `sorted` function is used with a `key` argument to sort the list of prefixes by their length. This is more efficient than sorting the list after generating all prefixes. 

Also, this solution runs in O(n^2) time, where n is the length of the string. This is because we are generating all possible prefixes of the string. If the string is very long, this function may be slow.