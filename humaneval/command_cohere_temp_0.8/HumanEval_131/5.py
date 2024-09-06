```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This Python script defines a function named `digits` that takes in a positive integer as an argument and calculates the product of its odd digits. The function first initializes a variable `prod` to 1, which will be used to accumulate the product of odd digits. Then, it iterates through each digit in the decimal representation of the input number `n`, checking if each digit is odd using the modulo operator (`int(digit) % 2`). If a digit is odd, it multiplies the `prod` by that digit. Finally, the function returns the value of `prod`, which gives the product of the odd digits of the input number.

This implementation is efficient because it avoids unnecessary conversions between numeric and string types. It is also concise and easily understood, making it well-suited for demonstrating the solution to the given problem. 

This code can be further improved for very large inputs (i.e., numbers with many digits), as it uses integer multiplication, which is not ideal for performance in such cases. Using `math.prod()` or `numpy.prod()` can offer a more efficient solution. 
```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod = prod * int(digit)
    return prod
``` 

This variation just modifies the way the odd digits are multiplied together.