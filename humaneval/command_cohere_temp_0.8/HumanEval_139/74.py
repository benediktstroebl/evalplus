Here's a Python script that defines the `brazilian_factorial` function as per the provided problem definition:
```python
def special_factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product
```

This function iteratively multiplies each integer between 1 and `n` to calculate the `brazilian_factorial`. The initial value of the `product` variable is set to 1 to ensure correct summation.

To test this function, you can use the following code that checks if the output is correct for the first few inputs:
```python
>>> special_factorial(0)
1
>>> special_factorial(1)
1
>>> special_factorial(2)
2
>>> special_factorial(3)
6
>>> special_factorial(4)
24
>>> special_factorial(5)
120
```

The provided code aligns with the problem's expectation, and the test cases validate its functionality.  This solution is efficient and readily accepts input to provide the corresponding Brazilian factorial value.  If you wish, we can further optimize this solution using predefined functions like `math.factorial` to enhance both readability and computational efficiency.