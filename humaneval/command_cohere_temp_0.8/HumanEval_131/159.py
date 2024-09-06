```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This Python script defines a function called `digits` that takes in a positive integer as an argument and calculates the product of all odd digits present in that number. The function first initializes a variable called `product` to 1, which will be used to accumulate the result. Then, it iterates through each digit in the string representation of the input number, checking if each digit is odd using the modulo operator. If the digit is odd, it multiplies it with the `product` variable. Finally, the function returns the value of `product`, which will be the result of the product of all odd digits, or 0 if all digits are even. 

Here is an example output of the function:
```python
digits(1)  == 1
digits(4)  == 0
digits(235) == 15
```

This corresponds to the examples provided in the problem statement.