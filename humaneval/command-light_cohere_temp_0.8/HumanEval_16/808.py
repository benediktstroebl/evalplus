```python
def count_distinct_characters(string: str):
    return len({c for c in string. characters() if c.isalpha()})
 str.

# Test case:
# Ensure all letters are lowercased
string = 'XYZ'
print(count_distinct_characters(string), "Count of distinct characters:", end())
```