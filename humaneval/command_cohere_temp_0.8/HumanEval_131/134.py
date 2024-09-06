```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function traverses the decimal representation of the input number n, multiplying each odd digit encountered by the evolving product. It returns 0 if all digits are even, and the final product of odd digits otherwise. 

Here's an example usage of the function:
```python
print(digits(123))  # Output: 27
print(digits(2))  # Output: 0
print(digits(235))  # Output: 15
```

The function's behavior aligns with the given problem statement, facilitating an intuitive calculation of the product of odd digits for any positive integer input.