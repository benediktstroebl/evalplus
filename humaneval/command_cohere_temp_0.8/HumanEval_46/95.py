```python
def fib4(n):
    a,b,c,d = 0,0,1,1
    for i in range(n):
        a,b,c,d = b,c,d, a+b+c+d
    return a
```

This script defines a function `fib4` that uses a loop to iteratively calculate the nth value of the Fib4 sequence for non-negative integer `n`. It uses assignments to regulate the accumulation of the four most recent terms of the sequence, ensuring that each term is correctly computed during the iteration. This avoids the need for recursion while efficiently calculating the Fib4 values. The result is a straightforward implementation that conforms to the specified problem requirements.