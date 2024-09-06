```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.count(c for c in string if c.isalpha()))
```
# Run the function with test inputs
# First, ensure that the string has some content
string = "Some content with mixed case characters"

# Now test the function
result = count_distinct_characters(string)
assert result == 4, "Function did not return expected count"

# Lastly, print the result
print("Distinct character count:", result)
```