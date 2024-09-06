```python
def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

def main():
    test_fib4()
```
The above code defines a function fib4 that computes the n-th element of the Fibonacci sequence using the recursive definition of the Fibonacci sequence:
1. The fib4 function takes an parameter n and returns the n-th Fibonacci number in the sequence.
2 The test_fib4 function tests the correctness of the fib4 function by asserting that the output of the function with the argument 5, 6, and 7 is equal to the expected values 4, 8, and 14, respectively.
3 The main function is the entry point of the program, and it simply calls the test_fib4 function to run the tests.

This code is self-contained, and does not require any additional input to compute the Fibonacci numbers or run the tests.