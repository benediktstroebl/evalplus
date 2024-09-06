Here's the self-contained Python script with a function `count_distinct_characters()` that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    # Remove all characters from the string, keeping only digits
    cleaned_str = ''.join(char for char in string if char.isdigit())
    
    # The count of distinct characters in the string is the length of the cleaned string
    return len(cleaned_str)
```