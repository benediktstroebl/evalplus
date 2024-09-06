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

def test_fib4():
    n = 7
    assert fib4(n) == 14

if __name__ == "__main__":
    test_fib4()
```
This code defines the function `fib4`, which calculates the nth element of the Fibonacci sequence using a loop-based approach. The function checks the initial conditions for n = 0 and n = 1, returning 0 and 1 respectively. Then, it uses the recurrence relation to calculate the other elements in the sequence. 

Finally, the `test_fib4` function is called to test the function with n = 7, which should produce the correct result 14.  The purpose of this code is to demonstrate how to implement a Fibonacci sequence function in Python, using a loop-based approach.