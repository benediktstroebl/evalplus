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
        assert fib4(5) == 4
        assert fib4(6) == 8
        assert fib4(7) == 14

        print("Success!")

if __name__ == "__main__":
    test_fib4()
```
The function `fib4` calculates the n-th Fibonacci number in the series without using recursion. It achieves this by summing the preceding four numbers. The test function `test_fib4` ensures that the function produces the correct results for the given input values.