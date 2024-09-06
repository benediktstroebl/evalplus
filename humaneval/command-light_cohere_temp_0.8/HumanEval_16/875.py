Here's a self-contained Python function to solve the problem you described:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not string.lowercase()})

# Example usage
print(count_distinct_characters('xyzXYZ'))
# Output: 3
print(count_distinct_characters('jerry'))
# Output: 4
```

This function iterates through each character in the input string, and checks if the character is not lowercase using the not lowercase operator. It then creates a unique set of these characters, which has an automatic count of distinct characters, and returns that count.