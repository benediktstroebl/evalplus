```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. The Fib4 sequence starts with 0 and 1, and the next number is the sum of the previous two numbers."""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    """Test the fib4 function by providing an integer n and expecting the n-th Fibonacci number."""
    test_case = 6
    expected = 8
    result = fib4(test_case)
    assert result == expected, f"The Fibonacci number for {test_case} is not {expected}, but got {result} instead."

if __name__ == "__main__":
    test_fib4()
```
The function `fib4` computes the n-th Fibonacci number by summing up the four previous numbers, which are calculated recursively. The test function `test_fib4` is used to check if the `fib4` function produces the correct Fibonacci number for a given input `n`.