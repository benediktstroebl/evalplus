Here's the self-contained Python function that passes the test cases:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```
The function uses a loop to iterate over every character in the input string. It checks if the the particular character, and increments the count if the character matches the given substring.