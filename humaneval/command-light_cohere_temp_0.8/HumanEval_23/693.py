Certainly! Here's a self-contained Python function that computes and returns the length of a given string: 
```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

# Testing the function
string1 = "" # An empty string
print(strlen(string1))  # Output: 0

string2 = "abc" # A string with characters
print(strlen(string2))  # Output: 3

string3 = "hello world" # A longer string
print(strlen(string3))  # Output: 11
``` 
This function, `strlen`, takes a string as input and returns the length of that string, as measured in Unicode code units. 

You can test the function using sample strings and verify that the output is indeed the length of the string.