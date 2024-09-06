```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of times the substring can be found in the original string. 
    1 match means it
    unique occurrences, no overlap.
    """
    string:str
    substring:str
    """
    return 1 + len(re.findall(substring, string))
```
Now, this function utilizes the re.findall function from the regular expression matching, which counts the number of unique occurrences of the substring in the original string.