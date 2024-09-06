```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n * n)
```

This function compares the input number x to the power of n when n is also an integer, and returns True if they are equal. It returns False if either condition is not met. 

The logic behind this solution is based on the idea that a number x is a simple power of n if it can be expressed as n^int, which simplifies to the notion that n raised to the power of int should yield the desired x. 

To test this script, you can call the function with different sets of inputs to see whether it returns true for simple power scenarios and false for non-simple power situations.