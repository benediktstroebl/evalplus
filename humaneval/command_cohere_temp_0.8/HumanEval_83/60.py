```python
def starts_one_ends(n):
    return (10 ** (n - 1)) * 9 + 1 - int((10 ** n - 1) / 9)
```

This Python script provides a function `starts_one_ends` that calculates the count of numbers that are `n-digit` positive integers starting or ending with 1.

The solution leverages the property that:
- Starting with 1, we have n-1 digits to fill with zeros or any digit not equal to 1 to result in a number less than or equal to 10^n-1.
- E.g., if `n` is 3, the number will look like `1xx`, where `xx` can be any two digits, giving us `10^2 - 1` or `9` options.

Other considerations:
- If the number ends with 1, we have n digits with n-1 zeros and 1, and the number will be less than or equal to 10^n-1.
- E.g., if `n` is 3, the number will look like `x1x`, where `x` can be any digit, giving us `10^3 - 1` or `10` options.

By subtracting the count of numbers that end with 1 from the count of numbers that start with 1 (as they are mutually exclusive), we arrive at the solution, i.e., `(10^(n-1)) * 9 + 1 - 10^n / 9`.