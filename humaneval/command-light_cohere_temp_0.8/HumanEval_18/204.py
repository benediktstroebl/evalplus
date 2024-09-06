Here is a self-contained Python function that finds the number of times a given substring can be found in the original string, while handling overlapping cases:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string, 
    while handling overlapping cases.
    """
    return sum(1 for i, j in zip(string, substring) if j == i)
``` 
This function uses a generator expression to iterate over every pair of characters in the string and substring simultaneously, and counts the occurrences where the corresponding characters match. 
The sum of the length of these overlapping matches gives the total number of occurrences of the substring in the string.