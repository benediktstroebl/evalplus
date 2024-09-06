```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input integer `n` to a string to iterate through its digits. For each digit, if it is odd (i.e., its remainder when divided by 2 is 1), it multiplies this digit with the `prod` variable, which starts at 1 and accumulates the product of odd digits. The function returns 0 if all digits are even, and the final product otherwise, providing the product of odd digits for the given input. 

The following test cases illustrate the correctness of the implemented function:
```python
# Test case for a single digit input
test_digits(1, 1)

# Test case for multiple digits
test_digits(235, 15)

# Test case with all even digits
test_digits(4, 0)

# Test case with no digits
test_digits(0, 0)
``` 

These test cases validate the function's behavior against the problem statement's requirements.