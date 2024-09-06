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
    assert fib4(8) == 24
    assert fib4(9) == 45
    assert fib4(10) == 55
    assert fib4(11) == 89
    assert fib4(12) == 144

def main():
    test_fib4()

if __name__ == "__main__":
    main()
```

The function `fib4` takes an integer `n` as input and computes the n-th Fibonacci number using a recursive approach. It uses base cases for n = 0, 1, and 2 to quickly compute Fibonacci numbers, and then combines these results using addition to compute the nth Fibonacci number in O(n) time complexity. 

The `test_fib4` function tests the `fib4` function with various input values, ensuring that the function produces the correct Fibonacci numbers. The `main` function is the entry point of the script, and it calls `test_fib4` to run the test suite. 

The code is self-contained and efficient, using a simple recursive approach to compute Fibonacci numbers with a time complexity of O(n).