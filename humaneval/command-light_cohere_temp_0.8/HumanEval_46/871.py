```python
def fib4(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    n = 7
    assert fib4(n) == 14  # Should evaluate to true

test_fib4()
```
This code defines a function called fib4 that computes the n-th Fibonacci number in the Fibonacci sequence using a simple formula-based approach. The formula used is not recursive but relies on previous values of the sequence.

It then defines a function called test_fib4 that tests the fib4 function with n=7, and verifies that the result is indeed 14. This test_fib4 function can be used to test the correctness of the fib4 function. 

Please note that this approach is not efficient for larger values of n because it uses an explicit formula, which can be computationally expensive.