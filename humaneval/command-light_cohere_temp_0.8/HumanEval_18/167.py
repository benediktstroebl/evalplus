Here is a self-contained Python function that solves the problem of finding the number of occurrences of a given substring within a string:
```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for _ in string. search(substring))
```
This function uses a generator expression to iterate over each character in the string, and for each character it checks if the character is equal to the substring. The function then counts the number of matches and returns the total count.