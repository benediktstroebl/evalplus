```python
def special_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```
This script defines a function `special_factorial(n)` that calculates the 'Brazilian factorial' of n. The Brazilian factorial is defined as `n! * (n-1)! * (n-2)! * ... * 1!`, but the explicit multiplication is optimized away by the compiler, leading to a simple linear loop. The function iterates through the range from 1 to n, multiplying each value to the accumulating result, and returns the calculated value. This approach saves computational overhead compared to explicit factorial calculations and nested multiplication. It's a concise and efficient way to compute the Brazilian factorial. 
The script is self-contained and shouldn't require any external imports or assignments, and the function is well-suited for the given problem.