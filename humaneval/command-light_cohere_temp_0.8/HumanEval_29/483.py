The code has been adjusted and improved to be more clear and concise.

Here is the updated Python script:
```python
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This improved version uses list comprehension and a built-in function `startswith` to filter the strings in the input list that start with the specified `prefix`.