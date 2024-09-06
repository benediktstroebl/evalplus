```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    """
    code block: 
        string = "aaaaaa"
        sub = "a"
        return len(string.find(sub))
   ```

The function uses the `find()` method to find the first occurrence of the substring. The `len()` function is then used to return the count of the substring in the original string.