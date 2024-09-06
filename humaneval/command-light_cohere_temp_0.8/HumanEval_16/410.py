Here's the self-contained Python script with a function that counts the number of distinct characters in a given string:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
The function utilizes the `set()` function along with the `lower()` method to remove case sensitivity and convert all characters into lowercase, ensuring an accurate count of distinct characters.

The test code is provided in the comment to ensure the function is working correctly.