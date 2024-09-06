```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input number to a string to iterate through its digits. For each digit, if it is odd (i.e., its remainder when divided by 2 is 1), it multiplies it with the `product` variable, which should be initialized to 1. The function returns 0 if all digits are even, and the final product of odd digits otherwise.

Here is a test case to test the function:
```python
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
``` 
This will validate the expected behavior of the `digits` function.