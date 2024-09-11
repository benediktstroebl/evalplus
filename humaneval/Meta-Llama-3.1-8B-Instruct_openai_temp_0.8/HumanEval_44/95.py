```markdown
### Change Numerical Base

This script changes the base of a given number.

#### Code

```python
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
    x (int): The number to convert.
    base (int): The target base.

    Returns:
    str: The string representation of x in base.
    """
    if x == 0:
        return '0'

    digits = []
    while x > 0:
        digits.append(int(x % base))
        x //= base

    return ''.join(map(str, digits[::-1]))


# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

#### Explanation

This script defines a function `change_base(x, base)` that takes an integer `x` and a base `base` as input. It returns the string representation of `x` in the given `base`.

Here's a step-by-step breakdown:

1. If `x` is 0, return '0' immediately.
2. Initialize an empty list `digits` to store the remainders of `x` divided by `base`.
3. Loop until `x` is 0:
   - Calculate the remainder of `x` divided by `base` using the modulo operator (`x % base`).
   - Append the result to the `digits` list.
   - Update `x` to its integer division by `base` using the floor division operator (`x //= base`).
4. Convert each digit in the `digits` list to a string using `map(str,...)` and reverse the list using slicing (`[::-1]`).
5. Join the strings in the list using the `join()` method to form the final string representation.

The test cases demonstrate the function's behavior with different inputs.