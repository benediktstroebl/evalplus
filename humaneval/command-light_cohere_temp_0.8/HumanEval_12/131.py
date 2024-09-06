```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the longest string in the list.
    >>> longest([])
    - None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a'])
    Traceback (most recent call last):
      File "<ipython-input-file-path>", line 5, in longest
      File "<string>", line 3:
    File "<ipython-input-file-path>", line 9, in long
        File "<type_names>.py", line 1207, in <module>
        File "<ipython-input-file-path>", line 1, in <module>
        File "<string>.makdown", line 8, in makdown
        File "<ipython-input-file-path>", line 34, in <module>
        File "<ipython-input-file-path>", line 35, in <module>
        File "<ipython-input-file-path>", line 36, in <module>
            File "<ipython-input-file-path>", line 40, in <module>

    >>> longest(['abc'])
    Traceback (most recent call last):
      File "<ipython-input-file-path>", line 5, in longest
      File "<string>", line 3:
    File "<ipython-input-file-path>", line 9, in long
        File "<type_names>.py", line 1207, in <module>
        File "<ipython-input-file-path>", line 1, in <module>
        File "<ipython-input-file-path>", line 42, in <module>
        File "<ipython-input-file-path>", line 43, in <module>

    """
    if not strings:
        return None
    max_len = 0
    for str in strings:
        if len(str) > max_len:
            max_len = len(str)
    return str(max_len)
```