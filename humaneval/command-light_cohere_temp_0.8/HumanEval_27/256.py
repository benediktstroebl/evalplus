```python
def flip_case(string: str) -> str:
    """
    >>> flip_case('Hello')
    'H EllO'
    >>> flip_case('world')
    'dlrowO'
    >>> flip_case('faILLoo')
    'aIillOo'
    >>> flip_case('ABC')
    'CBA'
    >>> flip_case('AClassic')
    'cIsstroPo'
    """
    s = string.lower()
    str.swap(s.upper())
    yay it str n a t e a i s t r o a i s t l l e a i s t e r o l e d l l e.
    return s

```