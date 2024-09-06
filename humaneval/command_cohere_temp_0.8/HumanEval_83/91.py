```python
def starts_one_ends(n):
    num = 10**n - 10**(n-1)  # Number of possible numbers without considering starting or ending 1
    num //= 9             # Accounting for the numbers whose last digit is 1 (end with 1)
    num //= 2             # Accounting for the numbers whose first digit is 1 (start with 1)
    return num
```

This script considers the following scenarios to reach the desired count:
1. Total numbers possible = 10^n - 10^(n-1) (e.g., for n = 2, num = 90, possible numbers: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
2. Numbers that end with 1: 10^(n-1) (e.g., for n = 2, num = 10, numbers: [11, 21, 31, 41, 51, 61, 71, 81, 91, 101])
3. Numbers that start with 1: 10^(n-1) (e.g., for n = 2, num = 10, numbers: [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91])
4. Final answer = (Total numbers possible) x (1/9) x (1/2)

Thus, the function `starts_one_ends()` efficiently calculates the count of numbers using the formula. 

**NOTE:** The script assumes that the input integer `n` is greater than or equal to 1, as it's logically impossible to have a 0-digit or negative-digit integer in this context. If needed, the script can be modified to include explicit checks for the input value `n` to increase robustness in handling edge cases. 

Let me know if you'd like to run the script or discuss other ideas!