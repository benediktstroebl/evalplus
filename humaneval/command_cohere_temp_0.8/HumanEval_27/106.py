```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses the swapcase function to convert all characters to the opposite case and leaves non-alphabetic characters unchanged. It joins the resulting characters back into a string and returns the modified string. 

To execute the function, simply call it with a string as an argument, like this:
```python
print(flip_case("Hello"))  # Outputs: hELLO
``` 

This will produce a string with the characters flipped as described in the problem prompt.