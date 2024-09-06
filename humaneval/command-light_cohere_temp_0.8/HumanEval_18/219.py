Here's the self-contained Python function that finds the number of times a given substring can be found in the original string, and passes the tests:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)
    for i in range(n):
        if string[i:i+m] == substring:
            count += 1
    return count
```
The function uses a loop to iterate over every substring of the original string. Then, it checks if the substring is present.