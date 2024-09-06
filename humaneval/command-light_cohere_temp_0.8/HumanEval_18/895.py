```python
def how_many_times(string: str, substring: str) -> int:
    return (string. string(). how_many_times_helper(string, substring))

def how_many_times_helper(string: str, substring: str) -> int:
    count = 0
    for char in substring:
        if char in string:
            count += 1
    return count
```