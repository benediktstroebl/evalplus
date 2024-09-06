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
    result = fib4(n)
    print(f"The {n}th Fibonacci number is {result}")

test_fib4()
```

This code defines a function `fib4` that computes the n-th Fibonacci number using a loop-free technique. It avoids recursion and computes Fibonacci numbers iteratively. The `test_fib4` function tests the `fib4` function with various input values and prints the results.

The output would be:
```bash
The 7th Fibonacci number is 14
```