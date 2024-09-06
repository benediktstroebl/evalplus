```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as an argument and returns a new string with flipped case letters—uppercase characters are converted to lowercase, and lowercase characters are converted to uppercase. The `swapcase()` method is used for the flip. Non-alphabetic characters like spaces, numbers, and symbols remain unchanged.

To test this function, you can use the following Markdown code block with an example and its expected result:
```python
>>> flip_case('Hello, World!')
'hELLO, wORLD!'
```

This should return 'hELLO, wORLD!' with flipped letters.

If you're interested in more coding challenges or tutorials, let me know the topic or concept you'd like to explore, and I'll be glad to provide further insights and guidance!