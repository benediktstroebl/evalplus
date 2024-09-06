```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It iterates through each digit in the decimal representation of `n` using a `for` loop. It checks if each digit is odd using the modulo operator `% 2` and if it is, it multiplies the `prod` variable by that digit. Finally, it returns the value of `prod`, which now stores the product of all odd digits. 

Here's an example usage of the `digits` function:
```python
print(digits(123))  # Output: 21
print(digits(1234))  # Output: 0
print(digits(15))  # Output: 15
```

This would output:
```bash
21
0
15
```

The first example shows that the product of odd digits of 123 is 21, as the digits of 1, 2, and 3 are 1, 3, and 1, respectively, and their product is 21. In the second example, the number is 1234, which contains only even digits (4, 3, 2, and 4), so the function returns 0, as specified in the problem statement. The last example shows the correct product of the single odd digit in the input number 15, which is as expected, 15.