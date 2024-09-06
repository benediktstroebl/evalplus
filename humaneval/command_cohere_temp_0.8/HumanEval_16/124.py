Here's a Python script that contains a function related to the task mentioned in the previous message:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store unique characters after converting each character in the input string to lowercase. This ensures that each character, regardless of the case, is treated equally. The `lower()` method is used to convert all characters in the string to lowercase. This way, the case of each character does not affect their uniqueness as asked in the prompt. Finally, the `len()` function is used to find the number of elements in the set, which corresponds to the number of distinct characters in the input string.