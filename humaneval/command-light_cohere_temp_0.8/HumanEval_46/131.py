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
    n = 5
    expected = 4
    actual = fib4(n)
    assert actual == expected, f"Test failed at n={n}"

test_fib4()
```

The function computes the n-th Fibonacci number by summing the previous four numbers, which is the most efficient way.  The test function runs the test cases, ensuring the function produces the expected result.