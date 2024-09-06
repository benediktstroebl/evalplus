Here's a self-contained Python function that solves the problem of joining a list of strings into a single string:
```python
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)
```
This function takes a list of strings as input and returns a single string by concatenating all the strings in the list. The code is self-contained, as it does not require external imports or depend on any other modules for its functionality.