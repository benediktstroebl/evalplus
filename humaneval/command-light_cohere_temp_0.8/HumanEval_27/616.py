```python
def flip_case(string: str) -> str:
    new_string = ''.join(''.join(c if c.isupper() else upper() else c.isupper() == True) string.
    return new_string.

# Test case 1
print(flip_case('Hello'))  # Output: hELLO

# Test case 2
print(flip_case('world'))  # Output: rOdlE

# Test case 3
print(flip_case('javascript'))  # Output: vrscript

# Test case 4
print(flip_case('Cohere AI is always ready to help!'))  # Output: Coere A I is always ra de