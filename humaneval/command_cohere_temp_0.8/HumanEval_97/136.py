```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as parameters. It extracts the unit digits of both numbers using the modulo operation (`modulo 10`, which returns the last digit repeatedly). It then computes the product of these unit digits and again takes the modulo of the result by 10 to ensure the answer lies between 0 and 9. The function ultimately returns this modified result. 

This approach to solving the problem is rooted in number theory and modular arithmetic. The modular arithmetic operation (`modulo` 10) allows us to focus on the last digit of each number, circumventing the need to consider the complete digits. This simplification makes it easier to manage and provides a more concise solution for the stated problem.