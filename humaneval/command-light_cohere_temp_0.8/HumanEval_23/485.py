```python
def strlen(string: str) -> int:
    return len(string)

# Testing the function with various inputs
string1 = "abc"
string2 = ""
string3 = "abc"
string4 = "hello"
string5 = "abc123"

print("Length of empty string:", strlen(string1))
print("Length of single character string:", strlen(string2))
print("Length before and after quote: ", strlen(string3))
print("Length of multi-character string:", strlen(string4))
print("Length of string with invalid characters:", strlen(string5))
```