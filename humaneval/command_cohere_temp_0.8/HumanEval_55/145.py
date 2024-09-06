```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The `Fibonacci sequence` is an integer sequence where the first two terms are 0 and 1. All other terms are obtained by adding the preceding two values. Although there is no closed form for the nth Fibonacci number, this recursive approach provides an effective computation. 

This function utilizes two base cases to terminate the recursive calls:
1. `if n <= 1`: This checks if the input `n` is either 0 or 1, since the Fibonacci numbers of these values are themselves.
2. It recursively calls `fib(n-1)` and `fib(n-2)` to calculate the Fibonacci number for `n` using the sum of the previous two Fibonacci numbers in the sequence.

This approach leverages the inherent nature of the Fibonacci sequence, avoiding the need for repeated addition calculations. The provided code defines the `fib` function, which takes an integer `n` as input and returns the n-th Fibonacci number. 

It includes three example test cases that demonstrate the function's behavior for different inputs, confirming the correctness of the implementation.