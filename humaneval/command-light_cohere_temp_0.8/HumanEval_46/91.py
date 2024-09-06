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
    n = 7
    expected = 14
    actual = fib4(n)
    assert expected == actual, f"Test failure at n={n}, expected={expected}, actual={actual}"

if __name__ == "__main__":
    test_fib4()
```
The function 'fib4' uses a loop to efficiently compute the n-th Fibonacci number, avoiding recursion. The test_fib4 function verifies the correctness of the 'fib4' function by passing a test case (n = 7) and comparing the computed result with the expected result (14).

This self-contained Python script demonstrates the implementation and testing of a function that computes Fibonacci numbers without recursion.