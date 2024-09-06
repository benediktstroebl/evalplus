Here's the function along with the test code:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns number of occurrences of substring in string.
    """
   
    string = "Hello, Python is awesome"
    sub = "LLO"
    return len(string.find(sub))
```

Output: