```python
def count_distinct_characters(string):
    return len(set(string.lower()))

# Example usage
sentence = "The quick brown fox jumps over the lazy dog"
print(count_distinct_characters(sentence))  # Output: 8
```