Here's a Python script that contains a function related to the task described in the code block provided:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store unique characters after lowering the input string, then returns the count of these distinct characters. This solves the problem of counting distinct characters in the provided markdown cell. It is also compatible with the example tests provided there.