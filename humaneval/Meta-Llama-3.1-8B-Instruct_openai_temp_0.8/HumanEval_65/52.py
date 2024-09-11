```markdown
### Circular Shift of Digits

This Python script solves the problem of circular shifting digits of an integer.

#### Code
```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
    x (int): The input integer.
    shift (int): The number of digits to shift.

    Returns:
    str: The result of circular shifting the digits of x as a string.
    """
    # Convert the integer to a string to easily manipulate digits
    str_x = str(x)

    # Calculate the actual shift, consider cases where shift > number of digits
    actual_shift = shift % len(str_x)

    # Split the string into two parts at the actual shift position
    first_part = str_x[-actual_shift:]
    second_part = str_x[:-actual_shift]

    # Combine the two parts to get the result
    result = first_part + second_part

    return result

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

#### Explanation

1. The `circular_shift` function takes an integer `x` and a shift value `shift` as input.
2. It converts the integer `x` to a string `str_x` to easily manipulate its digits.
3. It calculates the actual shift by taking the modulo of `shift` with the length of `str_x`. This handles cases where `shift` is greater than the number of digits in `x`.
4. It splits `str_x` into two parts: `first_part` (the last `actual_shift` characters) and `second_part` (the rest of the characters).
5. It combines `first_part` and `second_part` to get the result of the circular shift, which is then returned as a string.
6. The script includes test cases to demonstrate the function's behavior.