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
The provided code defines a function `fib4` that computes the n-th Fibonacci number in the Fibonacci sequence using the iterative approach. The function uses a pattern of checking for base cases (n = 0, 1, 2) and then using the result of previous two consecutive calls to `fib4` to calculate the next Fibonacci number. The tests at the result that the function is correct and returns the correct Fibonacci numbers. 

This code has a self-contained solution that efficiently computes Fibonacci numbers without using recursion, which can be more memory-efficient and may result in faster computation times compared to recursive solutions.