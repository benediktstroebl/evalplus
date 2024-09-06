```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(i) for i in string.
    # The tested by using list comprehension with string interpolation to create all possible prefixes
    # this method has a time complexity of O(n)
    # where n is the length of the input string
    # compared to the O(n^2) of iterative method
    # strings of length n can have at most n distinct prefixes
```