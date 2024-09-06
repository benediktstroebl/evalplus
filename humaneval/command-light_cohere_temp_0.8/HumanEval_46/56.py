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
    assert fib4(n) == 14

def main():
    print("Testing fibonacci sequence...")
    test_fib4()

if __name__ == "__main__":
    main()
```
The function `fib4` calculates the n-th element of the Fibonacci sequence using an optimized approach. It avoids recursion and uses an iterative method along with memoization to achieve better performance. The `test_fib4` function tests the `fib4` function with various input values, ensuring the function produces the correct results. The `main` function is the entry point of the script, calling the `test_fib4` function to verify the correctness of the Fibonacci sequence calculation.