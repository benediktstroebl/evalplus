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

def main():
    test_fib4()

if __name__ == "__main__":
    main()
```
The `fib4` function calculates the n-th element of the Fibonacci sequence using a loop- The function first checks if `n` is 0, 1, 2, or 3, and returns the appropriate value. If `n` is greater than 3, it recursively calls itself to calculate the previous four elements and then sums them up to get the Fibonacci number. The test_fib4 function tests if the `fib4` function with `n` equal to 7 returns 14, which is the correct Fibonacci number. The `main` function is the entry point of the script and calls `test_fib4` to run the test.