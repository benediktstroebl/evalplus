```markdown
### strlen Function

This Python function takes a string input and returns its length.

#### Code
```python
def strlen(string: str) -> int:
    """
    Return length of given string
    
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)
```

#### Explanation

- The `strlen` function takes one parameter `string`, which is a string type.
- The function uses the built-in `len` function in Python, which returns the number of items in an object.
- In the context of strings, `len` returns the number of characters in the string.
- The function then returns the length of the input string.

#### Example Use Cases

```python
# Test cases
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
print(strlen("Hello, World!"))  # Output: 13
```

### Usage

To use the `strlen` function, simply call it with a string as an argument and assign the result to a variable or print it directly.