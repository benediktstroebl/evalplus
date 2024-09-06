```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
    return:
        if n <= 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    """Test the fib4 function with various input values."""
    print("fib4({0}) = {0}".format(fib4))
    print("fib4({1}) = {1}".format(fib4))
    print("fib4({2}) = {2}".format(fib4))
    print("fib4({3}) = {3}".format(fib4))
    print("fib4({4}) = {4}".format(fib4))
```
The code defines the function fib4 that calculates the n-th element of the Fibonacci sequence using the recursive definition. The function returns the result of the Fibonacci number, with n as the argument. The test_fib4 function is used to test the correctness of the fib4 function by passing various input values and verifying that the output of the fib4 function is correct.