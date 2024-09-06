```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test the function
string1 = ""
string2 = "abc"
if strlen(string1) == 0:
    print("Test passed for empty string")
else:
    print("Test failed for empty string")

if strlen(string2) == 3:
    print("Test passed for non-empty string")
else:
    print("Test failed for non-empty string")
```