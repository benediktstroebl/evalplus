```python
def flip_case(string: str) -> str:
    """
    Converts a given string to have all characters flipped between lowercase and uppercase.
    Returns a string with characters in lowercase flipped to uppercase and vice versa.
    """

    idea is to use the string.re characteristic of all result of flipping between lowercase and uppercase
    """
    string = string.title()
    string = string.lower()
    its upper()
    string = string.title()
    lower

    lower()
    # return the string

# Test cases
test_string = "Hello"
test_string = "HeLLo"
print(flip_case(test_string))

test_string = "soaring EAGLE"
test_string ="uOScar"
print(flip_case(test_string))

test_string = "hello World!"
test_string ="HeLLo WorLD!"
print(flip_case(test_string))
```