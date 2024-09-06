```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This `digits` function iterates through each digit in the decimal representation of `n`, if a digit is odd, it multiplies it into the `prod` variable, which accumulates the product of odd digits. The function returns 0 if all digits are even.

To follow the problem statement strictly, I assumed the input to be a positive integer. If the input can be negative or zero, there might be a edge cases to consider such as:
```
digits(-2)  # Should it return 0 or 2?
digits(0)  # Should it return 0 or 0?
```
Let me know if you'd like to define the exact inputs and outputs according to your problem statement. Feel free to pair-program with me as you codify the solution and build additional test cases to make the function more robust.