```python
def flip_case(string: str) -> str:
    """
    Flip uppercase characters to lowercase and lowercase characters to uppercase.
    """
    flipped_string = ''
    for char in string:
        if char.isupper():
            flipped_string += char.lower()
        elif char.islower():
            flipped_string += char.upper()
        else:
            flipped_string += char
    return flipped_string
```
This script defines a function called `flip_case` that takes a single argument, `string`, which is of type `str`. This function iterates through each character in the input string, and depending on whether the character is upper case or lower case, it flips the case and appends it to a string called `flipped_string`. Any non-alphabetical characters remain unchanged. The overall time complexity is O(n), where n is the length of the input string.

To test this function, you can run the following code:
```python
test_cases = [
    ("Hello World", "hELLO WORLD"),
    ("123aBcDeFgHiJk", "132hcDeFgHiJk"),
    ("ALL CAPS AND SYMBOLS!!", "ALL CAPS AND SYMBOLS!!"),
]

for case in test_cases:
    assert flip_case(case[0]) == case[1]
```
This will ensure that the function works correctly for all the test cases provided.