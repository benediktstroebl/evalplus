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
    try:
        print(fib4(5))
        print(fib4(6))
        print(fib4(7))
    except Exception as e:
        print(f"Error: {e}")
```
The code defines a function `fib4` that computes the n-th element of the Fibonacci sequence using the recursive approach without recursion. The `test_fib4` function tests the `fib4` function by calling it with different values of `n`. The code then handles any exceptions that may occur during the testing process and prints an error message if needed.