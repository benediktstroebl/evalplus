```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It iterates through each digit in the decimal representation of `n` using a `for` loop. It checks if each digit is odd using the modulo operator `% 2` and if it is, it multiplies the `prod` variable by that digit. Finally, it returns the value of `prod`, which represents the product of the odd digits.

Here is a test case to ensure its functionality:
```python
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
``` 

This would ensure that the function operates correctly. 
This approach uses a basic iteration through the digits and leverages Python's implicit casting from string to integer, making it intuitive and concise. It provides a clear explanation of the logic and is efficient in terms of time and space complexity, following a linear pattern due to the digit iteration.