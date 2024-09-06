```python
def strlen(s: str) -> int:
    """Returns the length of a string."""
    return len(s)
```

This Python script defines a function called `strlen` that takes a string input (`s: str`) and returns the length of that string. It utilizes the built-in `len()` function to count the number of characters (including spaces, special characters, and punctuation) in the input string, effectively calculating the length of the string. 

The function is designed to follow the Python style guideline for function formatting, with the :str type hint indicating that the function expects a string as the input parameter. 

To use this function, you can simply call it and pass a string as an argument, and it will return the length of that string. 

For example: 

```python
print(strlen("Hello, World!"))
```

This will output: 

```
13
```

However, it's important to note that this function does not handle non-string inputs or invalid arguments gracefully. Adding proper input validation and error handling would make the function more robust and adaptable to real-world scenarios.