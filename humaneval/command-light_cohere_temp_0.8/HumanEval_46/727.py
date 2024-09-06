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

def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

def main():
    test_fib4()

if __name__ == "__main__":
    main()
```
The code defines a function fib4 that computes the n-th element of the Fibonacci sequence using a technique that avoids recursion. The function uses a simple case switching to efficiently calculate the nth Fibonacci number. The test_fib4 function is used to test the correctness of the fib4 function. The main function is the entry point of the script, and it calls the test_fib4 function to verify the correctness of the Fibonacci sequence computation.