Here is a self-contained Python script that defines a function `strlen` that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Test case 1
assertEqual('', strlen(''))
assertEqual(strlen(' '), 0)
assertEqual(strlen('abc'), 3)

# Test case 2
string1 = "hello"
string2 = ""
assertEqual(strlen(string1), len(string2))

# Test case 3
string1 = "hola"
string2 = "hello"
assertEqual(strlen(string1), len(string2))
```
This code provides a function `strlen` that takes a string as input and returns its length. It is also provides several test cases to ensure the correctness of the function's behavior.