Here's a Python script that contains a function to solve the problem and pass the tests:
```python
def count_distinct_characters(string: str) -> int:
    distinct_characters = set(string.lower())
    return len(distinct_characters)
```
The function `count_distinct_characters` uses a set to remove duplicate characters, and to handle cases insensitively. It then returns the length of the resulting set, which is the desired answer to the problem. You can use this function in the specified Markdown code block to test it.