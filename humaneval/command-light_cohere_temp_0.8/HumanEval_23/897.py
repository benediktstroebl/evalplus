Here is a self-contained Python script that defines a function strlen to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') 
    Traceback (most recent call last):
      File "<string>", line 10, in strlen
        File "<string>", line 5, in function '__main__'
        File "<ipython>.py", line 6, in function 'strlen'
        File "<string>", line 6: (Python 3.0 print(...))
   
    run in local server context but submitted remotely
    >>> len('abc')
    3
    """
    return len(string)
```