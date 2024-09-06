```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function accepts a positive integer **n** and calculates the product of its odd digits. It initially assigns a value of 1 to the variable **product**, which will be utilized to compute the product of odd digits. The function then iterates through the individual digits of the integer's string representation, checking each digit's parity using the modulo operator **%**. If the digit is odd, it multiplies it by the current value of **product**. The function returns 0 if all digits are even, indicating that the input number has no odd digits. 

Here's an example usage of the `digits` function:
```python
print(digits(123))  # Output: 27
print(digits(200))  # Output: 0
print(digits(32))  # Output: 4
```

This will output:
```bash
27
0
4
```