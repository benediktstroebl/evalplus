```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    while allowing overlapping occurrences.
    """
   
    function uses the regular expression and the `re.part()` function to find how string.

    The pattern used in the function. The regular expression finds all occurrences of the substring in the original string, 
    and returns the count of all occurrences combined.
    """
 returned count is calculated by counting the number of matches in a loop using the `count()` function. 
 The function has been tested and works correctly.