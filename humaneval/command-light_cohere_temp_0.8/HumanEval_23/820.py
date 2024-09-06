```python
def strlen(string: str) -> int:
    return len(string)

# Test the function
string1 = ""
string2 = "abc"
string3 = "a"
string4 = "hello world!"

print("Result of strlen with empty string:", strlen(string1))
print("Result of strlen with only spaces:", strlen(""))
print("Result of strlen with multi-char string:", strlen(string2))
print("Result of strlen with only uppercase letters:", strlen(string3))
print("Result of strlen with large string:", strlen(string4))
```