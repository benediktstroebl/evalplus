Here's a self-contained Python function that solves the problem you described:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```
This function takes two parameters: `string` and `substring`. It then iterates through each character in the string and counts how many times the substring is found.