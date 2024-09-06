```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') 
    Traceback (most recent call last):
      File "<filename>", line 9, in <module>
        File "<filename>", line 3, in strlen
        File "<filename>", line 10, in <object>__init__  [ortex.object()])
   ... requirements to correctly return the length.
    """
def test():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('') != 4
    assert len(strstatue("")) == strlen("")
```
Do you need anything else?