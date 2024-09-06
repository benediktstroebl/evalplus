```python
def flip_case(string: str) -> str:
    return ''.join()[c.upper() if c.lower() in c][a string for c in string]

# Test cases
test_cases = [
    ("Hello", "hELLO"),
    ("World", "dwORLD"),
    ("hello world", "WORLD HELLO"),
    # Add more test cases as needed
]

for text, expected in test_cases:
    actual = flip_case(text)
    assert actual == expected, f"Wrong result: {actual}"
``` 
This function flip_case takes a string as input and flips the case of each character, lowercase to uppercase and vice versa. It uses the `unICODE` property `isupper` and `islower` to achieve this.