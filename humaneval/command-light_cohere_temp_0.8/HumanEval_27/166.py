```python
def flip_case(string: str) -> str:
    """
    Convert a given string where characters are case-insensitive, 
    and return it.
    """
    `string` is a string, split into individual characters 
    then apply the following transformation: 
    All uppercase characters become lowercase 
    All lowercase characters become uppercase 
    Non- alphabetic characters remain unchanged.
    Returns the strings with the flipped case.

# test
print(flip_case("HELLO")) # output: Hello
print(flip_case("hello")) # output: hELLo
print(flip_case("abc123")) # Output: Abc123
print(flip_case("!!!@#$")) # Output: .#_@
```