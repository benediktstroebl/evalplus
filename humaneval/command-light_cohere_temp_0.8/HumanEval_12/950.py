```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Return the length of the longest string.
    strings = ['a', 'bb', 'ccc']
    return max(str(s).length())  # Test case 1
    strings = ['a', 'b', 'c']
    return max(str(s).length())  # Test case 2
    strings = ['a'] * 10  # Shuffle list
    return max(str(s).length())  # Test case 3
    strings = ['a', 'b', 'c'] * [i%3 for i in range(100)]  # Random list
    return max(str(s).length())  # Test case 4
    return None  # Test case empty list
```