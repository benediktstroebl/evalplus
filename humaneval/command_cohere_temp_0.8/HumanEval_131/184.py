```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This Python script defines a function named `digits` that takes in a positive integer as an argument and calculates the product of its odd digits. The function first initializes a variable `prod` to 1, which will be used to accumulate the product of odd digits. Then, it iterates through each digit in the string representation of the input number, checking if each digit is odd using the modulo operator (`%`). If a digit is odd, it multiplies it with the current value of `prod`. Finally, the function returns the value of `prod`, which now holds the product of all odd digits in the input number.

This solution is efficient because it progressively multiplies `prod` by each odd digit, avoiding the need for multiple multiplications. It also does not create any additional lists or containers, making it a lightweight solution for this problem.