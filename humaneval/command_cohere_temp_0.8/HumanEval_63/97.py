```python
def fibfib(n):
    prev1, prev2, fibfib_number = 0, 0, 0
    while n >= 3:
        fibfib_number = prev1 + prev2 + fibfib_number
        prev2, prev1 = prev1, fibfib_number
        n -= 1
    if n == 2:
        fibfib_number += prev2
    elif n == 1:
        fibfib_number += prev1
    return fibfib_number
```

The code employs a loop to generate the FibFib values, similar to the Fibonacci sequence. However, it adds the previous two values together rather than always pulling from the next sequence value. This adjustment is what creates the different sequence. As the loop generates each value, it stores the previous two values in the `prev1` and `prev2` variables. When the loop reaches the final three values, it performs a final calculation to generate the proper `fibfib_number` for the given input. 

This algorithm has a time complexity of O(2^n) because the loop runs until n becomes 2, and it computes the fibfib number iteratively using the previous two values.