```markdown
### Change Numerical Base of Input Number

#### Problem Description
Change numerical base of input number `x` to base `base`.

#### Code
```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
    x (int): The number to be converted.
    base (int): The target base (less than 10).
    
    Returns:
    str: The string representation of the number after conversion.
    """
    if x == 0:
        return '0'

    digits = []
    while x:
        digits.append(int(x % base))
        x //= base

    # Reverse the list of digits and convert to string
    return ''.join(map(str, digits[::-1]))

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

#### Explanation

*   We first handle the base case where `x` is 0, returning '0' immediately.
*   Then, we loop until `x` is 0, appending the remainder of `x` divided by `base` to a list of digits in each iteration.
*   After the loop, we reverse the list of digits and convert it to a string by joining the digits with an empty string.
*   Finally, we test the function with the provided test cases.
```