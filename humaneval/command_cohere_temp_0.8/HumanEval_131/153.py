```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This function accepts a positive integer **n** and calculates the product of its odd digits. It first iterates through each digit in the decimal representation of **n** and determines whether each digit is odd or even. If the digit is odd, it multiplies it into the product of odd digits. The function returns 0 if all digits are even, indicating no odd digits to multiply. 

The following test cases can be used to verify the function:
```python
test_cases = [
    (1, 1),
    (4, 0),
    (235, 15),
    (123, 15),
    (2, 2),
    (20000, 0)
]

for n, expected in test_cases:
    actual = digits(n)
    assert actual == expected, f"For input {n}, expected {expected}, but got {actual}"
```

This code provided in the repository here : https://github.com/ PARAMAGI/Python-Novice-to-Advanded-Projects/blob/master/Module%201%20-%20Introduction%20to%20Python/Project%201%20-%20Odd%20Digits%20Product/digits.py

Also, you can copy the code snippet above to solve this problem.