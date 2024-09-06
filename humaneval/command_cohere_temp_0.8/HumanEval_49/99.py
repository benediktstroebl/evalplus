```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` uses the `pow()` function to calculate `2` raised to the power of `n` modulo `p`, which is the required result for the given problem. It returns the result modulo `p` to ensure that it falls within the range of `p`, which is crucial, especially when dealing with large numbers and non-positive moduli. 

To use this code, you can add it to a Python script and call the function with the appropriate input values, such as `modp(3, 5)` to yield `3`, or `modp(1101, 101)` to return `2`. 

Note that this solution is concise and computationally efficient for positive integers `n` and `p`. However, if you encounter negative integers or require specialized numeric handling, you may need to consider additional use cases and edge cases.