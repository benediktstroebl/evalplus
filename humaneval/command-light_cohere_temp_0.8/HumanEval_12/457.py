```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one. """
    # Checks if input list is empty
    if not strings:
        return None
    # Shuffle the list to avoid worst case order
    strings.sort()
    particulars in the list to avoid worst-case behavior
    for i in range(1, len(strings)):
        strings[i - 1] = strings[i]
    # Sort strings in ascending order
    strings.sort()
    critical to make sure that the lengths will be consistent
    # Return the longest string
    return max(strings, key=len)

# Unit test
test_longest = []
test_longest.append(['a', 'bb', 'ccc'])
test_longest.append(['a'])
test_longest.append(['aa', 'bb'])
test_longest.append(['ccc'])
test_longest.append(['ab'])
test_longest.append([None])
test_longest.append(['abbb'])
test_longest.append(['c'])
test_longest.append(['ccc'])
test_longest.test_longest.append([])
test_longest.test_longest.sort()
test_longest)
```