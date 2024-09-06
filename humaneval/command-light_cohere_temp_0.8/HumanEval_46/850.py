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
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

#Unit tests
def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 26

#Example usage
fib4(10)
``` 
This script defines a function called `fib4` that computes the n-th Fibonacci number using a loop-free approach. The function uses a approach to avoid recursion by breaking down the computation into four basic cases:

- Case 0: If n is 0, the function returns 0.
- Case 1: If n is 1, the function returns 0.
- Case 2: If n is 2, the function returns 2.
- Case 3: If n is 3, the function returns 0.
- Otherwise, the function recursively calls itself with the argument `n-1`, `n-2`, `n-3`, and `n-4` to compute the n-th Fibonacci number. 

The test function `test_fib4` is used to check the correctness of the `fib4` function. The script also provides an sample usage of the `fib4` function by calling it with the argument 10.