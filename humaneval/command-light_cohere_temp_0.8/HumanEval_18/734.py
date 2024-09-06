Here's a self-contained Python function that finds the number of occurrences of a given substring within a given string, while also handling overlapping substring matches:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string. 
    while substring is found, increment count
    """
    count = 0
    i = 0
    j = 0
    while j < len(string):
        if string[j] == substring: 
            if i == len(substring):  # end of substring
                count += 1
            else:
                i += 1
            j += 1
        else: 
            j += 1
    return count
```
This code defines a function `how_many_times`, which takes two parameters: a string (`string`) and a substring (`substring`). The function uses a loop to iterate through the input string. It checks for each substring at each position and counts how many times it occurs while avoiding overlapping matches. This function efficiently solves thecount of occurrences of the substring within the string, providing a clear and readable solution.