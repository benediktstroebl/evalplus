```python
def fib4(n):
    a,b,c,d = 0,0,1,1
    for i in range(n):
        a,b,c,d = b,c,d, a+b+c+d
    return a
```

This script defines a function `fib4` that uses a loop instead of recursion to calculate the nth number of the Fib4 sequence, then tests the function against sample inputs. 

However, it's worth noting that this implementation has a time complexity of `O(2^n)` since the number of terms involved in the sum doubles with each iteration, which makes it not suitable for large inputs. If the input is large, it would be more efficient to use memoization, mathematical formulas, or matrix exponentiation to achieve a better time complexity.