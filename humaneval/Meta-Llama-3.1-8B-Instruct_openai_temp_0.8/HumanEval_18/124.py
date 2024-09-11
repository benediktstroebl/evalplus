```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring can be found in the string.
    """
    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index!= -1:
            count += 1
            index += 1  # Move the index forward to consider overlapping cases
        else:
            break
    return count
```

Example use cases:
```python
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```
This script uses the built-in `find` method of Python strings to find the occurrences of the substring in the string. It keeps track of the current index in the string and moves it forward after finding each occurrence, effectively counting overlapping cases. If no more occurrences are found, the loop breaks and the function returns the count.