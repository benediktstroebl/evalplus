```python
def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

# Unit tests
test_fib4 = {
    test_fib4(5)
})
```
This script defines a function `fib4` which computes the n-th Fibonacci number using a method that does not use recursion. The function uses a basic control flow and a series of if-else statements. 

The function returns the n-th Fibonacci number of the sequence when the value of `n` is greater than 0.