Here's a self-contained Python function that solves the problem you described:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    string = string.split(substring)
    length = len(string)
    for i in range(1, length):
        if string[i-1] == substring:
            count += 1
    return count
```
This function uses a for loop to iterate through each character of the string and count how many times the substring appears.