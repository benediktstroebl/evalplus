Here's a self-contained Python function that finds the number of times a given substring can be found in another string while avoiding overlapping cases:
```python
def how_many_times(text: str, sub: str) -> int:
    n = sub.size(text)
    return sum(1 for i in range(n))
```

This function uses a generator expression to count the occurrences of the substring within the text.