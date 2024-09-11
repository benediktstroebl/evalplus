```markdown
## Change Numerical Base of Input Number

### Problem Description

This script takes an input number `x` and changes its numerical base to a specified base `base`.
The result is returned as a string representation.

### Constraints

- Base numbers should be less than 10.
- Input number `x` is a positive integer.

### Solution

```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    :param x: Input number
    :param base: Desired base
    :return: String representation of x in base
    """
    
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Both x and base must be integers.")
    if not 2 <= base < 10:
        raise ValueError("Base must be between 2 and 9 (inclusive).")
    if x < 0:
        raise ValueError("Input number x must be a non-negative integer.")
    
    # Convert the number to base using a list to store the digits
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    # Reverse the list and convert it to a string
    return "".join(map(str, reversed(digits)))


# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

### Output

```
22
1000
111
```

### Explanation

The `change_base` function first checks if the input `x` and `base` are integers and if `base` is within the specified range. It then enters a loop where it calculates the remainder of `x` divided by `base` and appends the result to the `digits` list. The quotient of `x` divided by `base` is then assigned back to `x` and the loop repeats until `x` becomes 0. Finally, the function reverses the `digits` list, converts each digit to a string, and joins them together to form the final string representation of `x` in base `base`.