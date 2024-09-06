Here's a self-contained Python function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    return len(string)

#Test case 1:
assertEqual(strlen(''), 0)

#Test case 2:
assertEqual(strlen('abc'), 3)

#Test case 3:
assert len('abcde') == 5 

# Test case 4:
class_str = "this is a test"
assertEqual(strlen(class_str), 13)
```
This code defines a function `strlen` that takes a string as an argument and returns its length. The function is then tested against the provided test cases.