```python
def sort_even(l: list):
    """Sorts a list l such that values at even indices are sorted to
    be equal to the values of the corresponding even index in l, but in reverse.
    """
    return sorted(l)[::-1] # returns the list with even indexes values sorted to the reverse
```
 The function uses Python's built-in sorted() function with a reverse parameter to achieve the desired output.