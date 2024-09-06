```python
def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

def test_fib4():
    n = 7
    expected = 14
    actual = fib4(n)
    assert expected == actual, f"Failed asserting that {n}th Fibonacci number is {expected}, but got {actual}"

if __name__ == "__main__":
    test_fib4()
```

This script defines a function `fib4` that computes the n-th Fibonacci number using a loop-based approach. The function handles base cases for n equal to 0, 1, and 2, and recursively calculates the rest. The test function `test_fib4` is provided to check if the `fib4` function produces the correct Fibonacci number for a given input `n`. The script also includes a `main` block, where the `test_fib4` function is called to validate the function.