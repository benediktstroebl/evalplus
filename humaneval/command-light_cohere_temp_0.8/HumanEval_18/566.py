```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts occurrences of substring in string, without overlapping.
    Returns count of all unique occurrences.
    """
    optimized version with substring length and string length in consideration.
    """

    time complexity: O(n + m)
    space complexity: O(n + m)
    """
    n = len(string)
    m = len(substring)
    count = 0
    i, j = 0, 0
    while i < n :
        if string[i:i+m] == substring :
            count += 1
            i += m
        elif i + m < n : 
            j = i + m
            while j < n and string[j:j+m] == substring :
                count += 1
                j += m
            if j == n :
                break
    return count
```