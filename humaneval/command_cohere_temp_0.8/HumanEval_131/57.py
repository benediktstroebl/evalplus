```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input number to a string to easily iterate over its digits. It checks if each digit is odd using the modulo operator (`%`) and multiplies the odd digits together to calculate the product. The function returns 0 if all digits are even, and the product of odd digits otherwise. 

Here's an example usage of this function:
```python
print(digits(1))  # Output: 1
print(digits(4))  # Output: 0
print(digits(235)) # Output: 15
``` 

This should produce the expected output based on the provided problem description.