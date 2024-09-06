```python
def strlen(string: str) -> int:
    return len(string)

#Test cases
string = ""
assertEqual(strlen(string), 0)

string = "abc"
assertEqual(strlen(string), 3)

#Example usage
string = "Hello, World!"
assertEqual(strlen(string), 11)
```