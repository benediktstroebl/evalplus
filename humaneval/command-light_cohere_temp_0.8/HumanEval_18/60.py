```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Return the number of occurrences of the substring in the string, 
    counting overlapping occurrences as valid.
    """ 
    #s=set of(string.keys())
    using substring.
    for i in range(0, len(substring)):
        if substring[i] in s:
            return i+1
    return 0
    ```