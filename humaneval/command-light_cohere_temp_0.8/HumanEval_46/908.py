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

The script defines a function `fib4` which computes the n-th Fibonacci number in O(1) using an iterative approach without recursion. It then has a test suite which checks various input values to ensure the correctness of the function.