Here's the improved script with additional comments and a docstring to describe the function:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Determine the count of occurrences of a substring within the original string.
    >>> string = "This is a test string."
    >>> substring = "a"
    >>> how_many_times(string, substring)
    2
    >>> how_many_times("aaaaaa", "a")
    3
    """
    
    def count_ occurences():
        count = 0
        for char in string:
            if char == substring:
                count += 1
        return count
    
    return count_ occurences()
```