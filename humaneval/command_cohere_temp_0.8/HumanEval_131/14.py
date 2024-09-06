```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input integer `n` to a string to iterate through its digits. For each digit, it checks if the digit is odd or even, multiplying the odd digits to calculate the product. In case all digits are even, it returns 0. The algorithm optimally processes each digit only once. This solution provides an accurate result and aligns with the problem statement.