```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that takes a string as an input and returns a string with flipped cases for every character, leaving non-alphabetic characters unchanged. Case flipping is accomplished via the `swapcase()` method. This approach is both efficient and straightforward.

Here is an example usage of this script:
```python
print(flip_case("Hello World"))  # Output: "hELLO WORLD"
```

This code will print "hELLO WORLD" zestfully, with uppercase letters flipped to lowercase and vice versa. It's important to note that non-alphabetic characters like spaces, punctuation, and digits are left unaffected by this function, staying just as they are in the input string.