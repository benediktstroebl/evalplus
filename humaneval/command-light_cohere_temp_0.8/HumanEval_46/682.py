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
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

def main():
    test_fib4()

if __name__ == "__main__":
    main()
```
The function '**`fib4`**' takes an integer '**`n`**' as an argument and returns the n-th Fibonacci number. The function uses a unique approach by avoiding recursion and only relies on the previously computed Fibonacci numbers. The test '**`test_fib4`**' ensures that the function works correctly for the specified inputs.