```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```
This Python code defines a function `how_many_times` that calculates and returns the count of occurrences of a given substring within a given string. The function utilizes the process of searching for the substring within the original string using the `find` method from the string module. The result is designed to handle cases where the substring is found multiple times and cases where the substring is not present at all, providing a more comprehensive solution for the given problem.