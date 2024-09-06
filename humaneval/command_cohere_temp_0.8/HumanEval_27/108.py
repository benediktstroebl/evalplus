```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses a list comprehension to iterate through each character in the input string. When faced with alpha characters, it uses the `swapcase` method to interchange case. Meanwhile, any non-alpha characters are appended to the resultant string unaltered. The output is a string with flipped case for alphabetic characters. 

To see the function in action, call it with a string as an argument, like so:
```python
flip_case('Hello')  # Outputs: hELLO
``` 

This should verify that the function operates according to the problem statement. Feel free to ask any follow-up questions or request further assistance!