```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring within the original string.
    """
   
    simple approach using string slicing and a count loop:
    Counter overwrites each character of the substring into a list, then the length of the list is the number of occurrences.
    """return len(Counter(substring)(string))
```