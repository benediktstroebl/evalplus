```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The function `multiply(a, b)` takes two integers a and b as input, extracts the unit digits of both numbers using the modulo operation (`a % 10` and `b % 10`), then multiplies these unit digits and takes the modulo of the result by 10 to return the final answer.

To test this script, you can provide sample inputs and verify that the product of the unit digits matches the expected output for each test case. 
For example, let's test with the examples given in the problem statement:
1. `multiply(148, 412)` - The unit digit of 148 is 8 and 412 is 2, so the product is 8 * 2 = 16.
2. `multiply(19, 28)` - The unit digit of 19 is 9 and 28 is 2, so the product is 9 * 2 = 18. Then taking modulo 10 to return the final answer of 18 % 10 = 8.
3. `multiply(2020, 1851)` - The unit digit of 2020 is 0 and 1851 is 1, so the product is 0 * 1 = 0.
4. `multiply(14, -15)` - The unit digit of 14 is 4 and -15 is -5, so the product is 4 * -5 = -20. Then taking modulo 10 to return the final answer of -20 % 10 = 0.