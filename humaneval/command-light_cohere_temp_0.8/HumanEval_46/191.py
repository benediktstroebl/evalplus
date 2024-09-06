```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
    if n < 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    n = 7
    expected = 14
    actual = fib4(n)
    assert actual == expected, f"Failed at n={n}"

if __name__ == "__main__":
    test_fib4()
```
The code defines a Fibonacci sequence function that uses the mathematical formula to generate the next number in the sequence. The function starts with the base cases for n=0, n=1, and n=2, and then recursively calculates the next number in the sequence by summing up the four previous numbers. The test function `test_fib4()` takes an input `n` and calculates the Fibonacci number at that index using the `fib4()` function. The test then compares the expected result with the actual result, and asserts if they are equal. 

Please note that the code is designed to run without external dependencies and can be fully contained within the Python script.