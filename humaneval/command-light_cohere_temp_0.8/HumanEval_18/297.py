Here's the self-contained Python function to find the number of times a given substring can be found in the original string, while handling overlapping cases:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    while handling overlapping cases.

    Parameters: 
    string: The input string 
    substring: The substring to search for 
    Returns: The number of occurrences of the substring in the original string
    """
    count = 0
    index = string.find(substring)

    while index is not None:
        count += 1
        index += len(substring) - 1
        if index == len(string) - 1:
            break

    return count
``` 
The function finds the occurrences of a substring in the original string. The function utilizes the string. If there substring is found at the beginning of the string, it starts counting from the start of the substring.