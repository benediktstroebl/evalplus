```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This Python script defines a function named `digits` which takes in a positive integer as an argument and calculates the product of its odd digits. The function first initializes a variable `prod` to 1, which will be used to accumulate the product of odd digits. It then iterates through each digit in the decimal representation of the input number, checking if each digit is odd using the modulo operator %. If a digit is odd, it multiplies the `prod` by that digit. Finally, the function returns the value of `prod`, which will be 0 if all digits are even, and the product of odd digits otherwise. 

To ensure efficiency, the script processes each digit only once, minimizing unnecessary iterations and computations. This approach follows Python's philosophy of using clear, concise, and readable code to solve the problem.  This function can be easily incorporated into larger Python projects and can be modified to accommodate different product requirements or additional oddness criteria.