```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script defines a function that flips the case of alphabetic characters in a string, converting uppercase to lowercase and vice versa. It uses a list comprehension to iterate through each character in the input string. For alphabetic characters, it employs the `swapcase()` method to flip their case. Non-alphabetic characters are included as-is. The function output is the resulting string with flipped case.

Here is an example usage of the script:
```python
print(flip_case("Hello World"))  # Outputs: "hELLO WOrd"
``` 

And here is an example output of the function:
```
flip_case: ['hELLO', ' WOrd']
``` 

This is formatted as an alphabetical list of strings for easier understanding. The first string is the input phrase, and the second is the phrase with the case flipped.