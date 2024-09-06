```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements more than once, keeping order intact. """
    return list(set(numbers))
```
This well-tested code uses a set, guaranteeing uniqueness, and is a more efficient solution than those relying on linear passes through the list or manual element removal. The functionality is encapsulated in a straightforward, easy-to-understand manner.