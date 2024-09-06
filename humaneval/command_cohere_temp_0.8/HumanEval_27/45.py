```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.islower() else c for c in string)
```

This script provides a function that takes a string as an input and flips the case of the characters, making sure that uppercase characters remain the same while lowercase characters are flipped to uppercase and vice versa. This behavior is achieved through the use of the `swapcase()` method and a conditional check using `islower()`. The function then joins the characters back together into a single string, resulting in the desired case flip transformation. 

To further validate the functionality of this script, you can test it with various inputs, such as 'hello', 'Nice Day', or even custom strings, to ensure that the result matches the desired case flip transformation.