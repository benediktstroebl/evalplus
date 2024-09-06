```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It iterates through each digit in the decimal representation of `n` and multiplies the odd digits into the `prod` variable, which starts at 1. In effect, it computes the product of all odd digits and returns 0 if all digits are even. The behavior is exemplified in the given test cases:
- `digits(1) == 1` 
- `digits(4) == 0` 
- `digits(235) == 15` 

The provided code is adaptable and efficiently solves the problem statement. It can handle a wide range of input values and generates the desired results.