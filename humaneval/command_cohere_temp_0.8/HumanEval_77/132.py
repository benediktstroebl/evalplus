```python
def iscube(a):
    return a ** (1/3) == int(a ** (1/3))
```
This function simplifies the equation to a single equality operation and uses the `int()` function to evaluate the cube root of the integer a, which allows for a quick comparison to determine if the number is a perfect cube or not. 

This is an optimization of the solution using `math.sqrt()` and `math.pow()` which might lead to a wrong result due to the double precision of the floating numbers.