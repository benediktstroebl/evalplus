Here is a self-contained Python function that solves the problem of finding how many times a substring can be found in the original string, while also checking for overlapping substring matches:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while avoiding overlapping.
    Return value of the example returns the number of positions where the substring appears.
    """
   

    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            return i
    return len(string)
```
This function implements a loop that checks for the substring at each possible position, and returns the position where the substring is found. The tests for the a simple input validation and a basic test case.