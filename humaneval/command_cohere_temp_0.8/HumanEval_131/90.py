```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This Python script defines a function called `digits` that takes in a positive integer as an argument and calculates the product of its odd digits. The function first initializes a variable called `prod` to 1, which will be used to accumulate the product of odd digits. Then, it iterates through each digit in the decimal representation of the input number `n` and checks if the digit is odd using the modulo operator %. If the digit is odd, it multiplies the `prod` by the value of that odd digit. Finally, the function returns the value of `prod`, which gives the product of the odd digits of the input number.

Here's an example of how you can use this function:
```python
result = digits(235)
print(result)  # output: 15
```

This will produce the expected output of 15, which is the product of the odd digits of the input "235".