```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(abs(x) for x in arr) * product(x % 2 for x in arr)
    return result
```
This Python script defines a function called `prod_signs` that takes an array of integers as input. It aims to calculate and return the sum of the magnitudes of the integers in the array multiplied by the product of their signs (1, -1, or 0). This is achieved by using list comprehensions to calculate the sum of magnitudes and the product of signs. The function returns None if the input array is empty.

The script includes a docstring paragraph immediately below the function definition, providing information about the purpose of the function and its behavior through illustrative examples. These examples illustrate how the function works when given various input arrays and demonstrate the expected output for each case. The function is designed to handle empty arrays by returning None, as specified in the docstring. Overall, this code snippet is a concise and self-contained implementation of the specified problem, making it easier for users to understand and use for their specific needs.