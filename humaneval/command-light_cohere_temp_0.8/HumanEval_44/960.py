```python
def change_base(x: int, base: int):
    """
    Change the base of integer x to base b, 
    and return the string representation.
    """
    number = str(x)
    if len(number) == 1:
        return number
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    sign = '+' if x < 0 else ''
    while len(number) < base:
        digit = get_digit(number, len(number))
        number = f"{sign}{digit}{number[len(number) - 1]}{base}"
    return number

def get_digit(numstr, index):
    """Convert a string numstr into a list of digits, 
    starting from index, and return the nth digit."""
    return [int(char) for char in numstr[index:]]

test_change_base = [
    ("8", 3),  # invalid base
    ("90", 2),  # invalid input
    (5, 2),   # invalid input
    ("12", 10),  # decimal input
]

for case in test_change_base:
    try:
        result = change_base(*case)
        assert result == str(case[1])
    except AssertionError as e:
        print(f"Test case ({case[0][0]}, {case[1]}) failed: {e}")
```
This script defines a function change_base that takes an integer x and an integer base as input and returns the string representation of x in the desired base. It also includes a test cases to verify the correctness of the function. The test cases cover a following: invalid base, invalid input, and decimal input. The function is tested using the test cases, and the test passes if it doesn't raise an exception.