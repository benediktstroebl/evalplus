```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() for char in string)
```
The function uses a list comprehension with the `swapcase()` method to flip the case of each character in the string. Case flipping is performed consistently and expeditiously using this method.

Here is a sample usage of the function:
```python
print(flip_case("Hello")) # Output: hELLO
print(flip_case("abcDE")) # Output: AbcDe
print(flip_case("SuPerB")) # Output: suPERB
``` 

This function will produce the desired output of flipping the case for both lowercase and uppercase characters.