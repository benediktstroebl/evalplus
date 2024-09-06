```python
def choose_num(x, y):
    max_even = max((z for z in range(x, y+1) if z % 2 == 0), default=-1)
    return max_even
```

The Python script uses a few techniques worth explaining:
1. **Even Filtering**: The snippet uses a generator expression with the `range` function and a filtering condition (`z % 2 == 0`) to generate only even integers between `x` and `y`, inclusive. This sequence is then passed to the `max` function, which returns the highest value in the sequence. The `default=-1` argument ensures that if no even numbers are found in the range, the function returns -1. 
2. **Max Function**: The Python `max` function is used to determine the highest even number. If the generator expression produces no even numbers, the default value (-1) is triggered, and the function returns -1. 

This approach allows the function to work independently, cleanly, and efficiently for the given problem. 

The code can be enhanced with additional tests to validate edge cases, and the comments can provide more detailed explanations of the underlying algorithmic and mathematical principles. 

Please let me know if you'd like me to expand the test suite or provide more context on specific aspects of the solution.  Hope this helps!