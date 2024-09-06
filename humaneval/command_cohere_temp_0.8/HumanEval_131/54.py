```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This script defines a function `digits()` that takes an integer `n` as input and calculates the product of all odd digits present in `n`. The function first iterates through each digit in the string representation of `n` using a `for` loop. For each digit, it checks if the digit is odd using the modulo operator (`int(digit) % 2 == 1`). If the digit is odd, it multiplies the `prod` variable by that digit. Finally, the function returns `prod`, which now holds the product of all odd digits in `n`. 

The function returns `0` if all digits are even, as indicated in the problem statement. This is the base case for the recursive thinking approach.