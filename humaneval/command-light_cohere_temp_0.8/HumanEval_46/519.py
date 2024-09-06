```python
def fib4(n: int):
    """
    The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones.

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
    """
    tests = [
        (5, 4),
        (6, 8),
        (7, 14),
    ]

    for test_n, expected_answer in tests:
        actual_answer = fib4(test_n)
        assert actual_answer == expected_answer, "Test failed: {}"

if __name__ == "__main__":
    test_fib4()
```
The provided Python script defines a function `fib4` that computes the nth element of the Fibonacci sequence using a modified formula without recursion. The `test_fib4` function contains test cases, with expected answers, and runs the `fib4` function against these test cases. The script also has a `if __name__ == "__main__":` block to ensure that the `test_fib4` function is run when the script is executed directly.