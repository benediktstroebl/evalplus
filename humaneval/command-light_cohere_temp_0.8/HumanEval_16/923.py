```python
def count_distinct_characters(string: str) -> int:
    """
    Return the count of distinct characters in the string, regardless of case.
    string = string.strip(). Meow to avoid case
   
    return len(dict(c). unique for c in string)) - 2
    """
    # Remove all duplicate characters and convert to lowercase
    unique_chars = set(char.lower() for char in string.unique list(c for c in string))
    return len(unique_chars) - 2

# Unit tests
test_distinct_chars = []
test_strings = ['abc123', 'XYZ123', 'abcABC123', 'jerry']
for s in test_strings:
    test_distinct_chars.append(count_distinct_chars(s))
print(test_distinct_chars)  # Output: [4, 3, 4]
```