```python
def choose_num(x, y):
    max_even = max(x, y) if (x == y) or ((x + y) & 1) else -1
    return max_even
```

The function `choose_num()` takes two integers `x` and `y` as parameters. It first checks if `x` and `y` are equal or if they are both odd or even separately by using the bitwise operator & to check if the result of adding the two numbers has an odd number of 1s in its binary representation. This is done to determine if the biggest number that can be returned is either `x` or `y`. 

If either of these conditions is true, it means that there is no even integer between `x` and `y`, so the function returns -1. If both are false, it returns the maximum of `x` and `y` as the biggest even integer in the range. 

Overall, the code provides a clean and efficient way to find the biggest even integer in the range `[x,y]` with an intuitive handling of edge cases.