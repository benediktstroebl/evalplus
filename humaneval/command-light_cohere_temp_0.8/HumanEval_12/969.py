```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string in the list.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['aa', 'b'])
    'aa'
    >>> longest(['aa', 'bb', 'a'])
    'aa'
    """
    return max(strings, key=len)
``` 
This version ensures self-containment by not using any external Python libraries, which makes it more suitable for embedding in Markdown code.