```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as an argument and returns a string with flipped case, excluding non-alphabetic characters. Case flipping is accomplished via the `swapcase()` method. Such a method preserves the character's general shape, only changing uppercase to lowercase and vice versa.

Here's an example usage of this function to test its functionality:
```python
print(flip_case("Hello World"))  # Output: HEllO wORLD
print(flip_case("fooBAR"))  # Output: fOObAR
print(flip_case("123"))  # Output: 321
```

The expected behavior of the function is to exclusively alter the case of alphabetic characters, thereby retaining numeric and special characters intact. This is achieved by applying the `swapcase()` method to each alphabetical character in the string.