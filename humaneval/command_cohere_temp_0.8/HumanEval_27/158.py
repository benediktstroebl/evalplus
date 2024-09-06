```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses the swapcase function to convert all characters to the opposite case and leaves non-alphabetic characters unchanged. It joins the resulting list of characters into a string to produce the desired 'hELLO' output for the example input 'Hello'.