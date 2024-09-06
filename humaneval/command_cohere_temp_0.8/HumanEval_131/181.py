```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This problem can be solved by converting the input n into a string to iterate over each digit. We check if each digit is odd or even, updating a variable prod that accumulates the product of odd digits. The final value of prod will be 0 if all digits are even, and the product of odd digits otherwise.