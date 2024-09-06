```python
def strlen(string: str) -> int:
    return len(string)

# Testing the function
string1 = ""
assert strlen(string1) == 0

string2 = "abc"
assert strlen(string2) == 3

string3 = "abcabc"
assert strlen(string3) == 3

# Main usage
# Test the function with different inputs
result = strlen("def")
print(result)  # Output: 8
```