```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This function uses the `set()` method along with `lower()` to ensure all characters are lowercase and treat each character as a distinct entity in the set, thereby counting the number of distinct characters. 

This is a common and simple approach to solving this problem.