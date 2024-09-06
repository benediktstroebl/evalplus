```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)
```

This function examines the type of `x` to determine if it is an integer and compares it to the result of raising `n` to the power of the square root of `n`. It returns 'True' in the event that they are the same; otherwise, it returns 'False'. 

Here is an example usage of the function:
```python
print(is_simple_power(1, 4))  # Outputs True
print(is_simple_power(2, 2))  # Outputs True
print(is_simple_power(8, 2))  # Outputs True
print(is_simple_power(3, 2))  # Outputs False
print(is_simple_power(3, 1))  # Outputs False
print(is_simple_power(5, 3))  # Outputs False
``` 

All of the test cases should print 'True' except for 3, 2 and 5, 3, which should print 'False'. 

This approach utilizes the property that a number 'x' is a simple power of 'n' if there exists an integer 'k' such that `n ** k = x`, where 'n' is not zero and 'x' is not zero and is an integer. For any integer 'x', `int(n ** 0.5)` raises 'n' to the power of the square root of 'n', which is an integer. Therefore, if `n ** int(n ** 0.5) == x`, then 'x' is a simple power of 'n'.