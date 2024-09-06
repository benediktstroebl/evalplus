Here's a Python script that contains a function related to the task described in the code block:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses a set to store the distinct characters in the string after converting all characters to lowercase. The `lower()` method is applied to convert all characters to lowercase. Then, the `set()` function is used to remove any duplicate characters, leaving only distinct characters. Finally, the `len()` function is used to count the number of distinct characters in the set, which is then returned as the result.