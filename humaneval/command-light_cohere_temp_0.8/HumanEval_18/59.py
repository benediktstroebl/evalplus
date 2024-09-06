Here is a self-contained Python function that finds the number of times a given substring can be found in the original string, while accounting for case where the substring is longer than the original string:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    string = string.sub(substring)  # Use a shorter substring to find the match

    while string:
        if substring in string:
            count += 1
        string = string.split('', 1)[0]  # Move to next character to find a possible match

    return count
```