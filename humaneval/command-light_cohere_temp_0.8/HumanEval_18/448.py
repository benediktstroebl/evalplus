Here's the self-contained Python function:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    len_string = len(string)
    for i in range(len_string):
        if string[i] == substring:
            count += 1
    return count
```
The function takes two parameters: `string` and `substring`. It uses a loop to iterate through each character of the `string`. It checks if the current character is equal to the `substring`. It increments the count if they match and adds 1 to the count variable. 

This function can be used to find the frequency of a substring within a given string.