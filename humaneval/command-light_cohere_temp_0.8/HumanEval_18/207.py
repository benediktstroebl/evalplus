```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring using sliding window. 
    O(n) -> n/2 space efficient.
    """
   
    best case:
    - For an input 'abc...' and 'a', the first window has 2 elements and the second window has 1 element. 
    - Then best worst case:
     6 elements and no overlap.
    """
    `def how_many_times(str, sub):
    """
        Counter for the substring in the string
        Returns the number of occurrences of substring in str
        """
    count = 0
    sub_len = len(substring)
    string_len = len(string)
    window = [0] * sub_len
    for i in range(string_len - sub_len + 1):
        window[i % sub_len] += 1
        count += window[i]
        window[i] = 0
    return count
```