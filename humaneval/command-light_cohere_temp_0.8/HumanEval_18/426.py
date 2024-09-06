```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    """
    string = "hello"
    sub = "ll"
    n = 0
    i = 0
    while i < len(string):
        if string[i] == sub:
            n += 1
        i += 1
    return n
# Example:
print(how_many_times("hello", "ll"))
```