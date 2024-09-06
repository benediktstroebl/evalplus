```python
def flip_case(string: str) -> str:
    return string.case_flip(string.case_flip("hello"))
```

This script defines a function called `flip_case` that takes a string as input and returns a string with the characters' case flipped. The function uses the name `case_flip` for a built-in function that flips the case of each character in the string. This helps in passing the case transformations to a given string.