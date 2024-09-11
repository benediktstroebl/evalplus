```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return sorted(prefixes, key=len)


# Test the function
print(all_prefixes('abc'))  # ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # ['h', 'he', 'hel', 'hell', 'hello']
print(all_prefixes('xyz'))  # ['x', 'xy', 'xyz']
```

This script defines a function `all_prefixes` that generates all prefixes of a given string and returns them in order from shortest to longest. The function uses a loop to iterate over the indices from 1 to the length of the string, and for each index, it appends the substring from the start of the string to the current index to the list of prefixes. The `sorted` function is then used to sort the list of prefixes by their lengths, effectively ordering them from shortest to longest. The function is then tested with three example strings.