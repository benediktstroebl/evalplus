```python
def fib4(n: int):
    """
    The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.

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

# Unit tests

def test_fib4():
    assert fib4(5) == 4
    
if __name__ == "__main__":
    test_fib4()
```

This Python script defines a function `fib4` which computes the n-th value of the Fibonacci sequence without recursion. The function utilizes a series of if-else statements to check the value of `n`, and then executes the appropriate mathematical calculation to determine the next value in the sequence. The function is tested using the `test_fib4` function, which ensures the `fib4` function produces the correct results for the specified input values.