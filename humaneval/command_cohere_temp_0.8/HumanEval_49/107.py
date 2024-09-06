Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as parameters, n and p, and employs the Python built-in function pow to compute 2 raised to the power of n modulo p. This solution is concise and leverages the built-in capabilities of Python to handle modular exponentiation efficiently.

To test this function, you can execute it with different input values and verify that it produces the expected results as shown in the given problem statement. Here's an example:
```python
modp(3, 5) # 3
modp(1101, 101) # 2
modp(0, 101) # 1
modp(3, 11) # 8
modp(100, 101) # 1
```
This demonstrates that the function behaves as expected according to the given tests, producing outputs of 3, 2, 1, 8, and 1, respectively. 
Please note that this solution assumes realistic inputs where overflowing integers isn't a concern. If you encounter potential integer overflow issues, consider using a different approach or mitigating techniques.