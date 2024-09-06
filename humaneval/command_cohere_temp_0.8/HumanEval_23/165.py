```python
def strlen(s: str) -> int:
    """Returns the length of a string."""
    return len(s)
```

This Python script defines a function named strlen that takes a string s as an argument and returns the length of that string. It utilizes the built-in Python function len to determine the number of characters in the input string. The function is encapsulated in a self-contained code block, and it appropriately handles the task of calculating the length of a given string. 

Here is an example of how to test this function:
```python
# Test the function with one example
assert strlen("test") == 4

# Test the function with another example
assert strlen("hello") == 5
```

This will correctly verify that the `strlen` function works as expected, accurately calculating the length of the given strings.