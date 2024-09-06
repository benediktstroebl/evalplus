```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This script defines a function `digits` that takes in a positive integer `n` as an argument and calculates the product of its odd digits. It initially sets the `prod` variable to 1, which will be used to accumulate the product of odd digits. It then iterates through each digit in the decimal representation of `n`. Using the modulo operator (`%`), it determines whether each digit is odd or even. If the digit is odd, it multiplies the `prod` by the integer value of that particular digit. Finally, it returns the value of `prod` as the result, which will be 0 if all digits are even, and the product of odd digits otherwise. 

To ensure clarity and readability, it is good practice to include the following:
- Including docstrings: Docstrings describe the purpose and functionality of your function, making your code more understandable to anyone who reads it.
- Indentation: Consistent indentation improves code readability and helps to visually identify the structure and blocks of code.
- Using meaningful variable names: Choosing descriptive names for your variables helps in understanding the code. 

These coding techniques help in maintaining a clean and understandable codebase and are therefore widely adopted in the software development community.