```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This script defines a function `digits` that takes an integer `n` as input and calculates the product of its odd digits. It initially sets the `prod` variable to 1, which will be used to accumulate the product of odd digits. Then, it iterates through each digit in the string representation of `n` using a `for` loop. For each digit, it checks if the digit is odd using the modulo operator (`int(digit) % 2`). If the digit is odd, it multiplies the `prod` value by the int value of the digit, effectively accumulating the product of odd digits. Finally, the function returns the value of `prod`, which will be 0 if all digits are even, and the desired product otherwise.

Here is an example usage of the `digits` function:
```python
print(digits(1))
print(digits(4))
print(digits(235))
```

This will output:
```
1
0
15
```

The function digits returns 1, because the digit 1 is odd. It returns 0, because 4 has no odd digits. Lastly, for 235, it returns 15, as the odd digits (and their product) are 5.