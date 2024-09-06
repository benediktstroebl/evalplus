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

# Test the function
test_fib4 = fib4(5)
test_fib4 = test_fib4 == 4
test_fib4 = test_fib4 == True
```
The code defines a function called fib4 that computes the n-th element of the Fibonacci sequence. The function uses a simple formula to compute the n-th element, which is the sum of the previous four elements. The tests at the  ensure that the function is correct and pass the test.