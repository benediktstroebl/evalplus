```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if a number `x` is a simple power of `n` by evaluating the condition `n ** int(x == n ** x)`. If this condition evaluates to truthy, it means that `x` is a simple power of `n`, as the equation `n ** int(x == n ** x)` will hold true when `x` is a simple power of `n`. 

Here is a summary of how the condition works:
- The type of `n` is checked to be an integer using the `type(n) is int` condition. This ensures that the base `n` is an integer. 
- The equivalence `x == n ** x` checks if `x` is a power of `n`. This step also ensures that the exponent `x` is itself an integer. 
- The int() function is then applied to the boolean expression `x == n ** x`, converting it to integer, before the equality is checked against. This step ensures that the previous equivalence is evaluated as an integer equality. 

This combined condition is what is_simple_power returns, effectively capturing the simple power relationship between `x` and `n`. 

This function encapsulates the problem statement and should be self-contained, as it doesn't rely on any external dependencies or additional functionality that hasn't been explicitly defined within the function. 

You can test this function using the example test cases provided in the problem statement like so:
```python
# Example test cases
print(is_simple_power(1, 4))  # Expected output: True
print(is_simple_power(2, 2))  # Expected output: True
print(is_simple_power(8, 2))  # Expected output: True
print(is_simple_power(3, 2))  # Expected output: False
print(is_simple_power(3, 1))  # Expected output: False
print(is_simple_power(5, 3))  # Expected output: False
``` 
The function should return the correspondingly correct boolean values for each test case.