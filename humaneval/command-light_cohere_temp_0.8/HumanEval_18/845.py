Here's the self-contained Python function that solves the problem:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string.
    :param string: str, the original string
    :param substring: str, the substring 
    :return: int, the count of the substring
    """
    count = 0
    n = len(string)
    m = len(substring)
    for i in range(n):
        if string[i] == substring:
            count += 1
    return count
```
The function takes two parameters: `string`, which is the original string, and `substring`, which is the substring to search for. The function then uses a loop to iterate through the original string and counts the number of times the substring is found.