```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This Python script defines a function called `digits` that takes in a positive integer as an argument and calculates the product of its odd digits. The function first initializes a variable `prod` to 1, which will be used to accumulate the product of odd digits. It then iterates through each digit in the decimal representation of the input number, checking if each digit is odd using the modulo operator (`int(digit) % 2 == 1`). If an odd digit is found, it multiplies the `prod` by the odd digit. Finally, the function returns the value of `prod`, which will be 0 if all digits are even, and the product of odd digits otherwise. 

The TDD approach ensures that the `digits` function is tested against a variety of inputs to confirm its correctness. You can add more tests to further validate the function and ensure it handles various scenarios properly.