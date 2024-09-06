```python
def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string in a list, or None if empty. """
    - Returns list of strings of length 1
    - Return the string if all lengths are the same
    - Otherwise, return None.

>>> longest(['a'])
'a'

>>> longest(['a', 'b'])
'b'

>>> longest(['a', 'bb'])
'bb'

>>> longest(['a', 'bb', 'ccc'])
'ccc'

>>> longest([])
None

>>> longest(['a', 'bc'])
'bc'

```