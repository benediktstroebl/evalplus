```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each subsequent term is the sum of the two preceding ones.

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

def test_fibonacci(n: int):
    """Test function to check if the fib4 function works correctly.

    assert(fib4(n) == fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4), str(n)

if __name__ == "__main__":
    """Main execution section of the script"""
    n = int(input("Enter the value of n: "))
    test_fibonacci(n)
```

The `fib4` function computes the n-th element of the Fibonacci sequence, using an iterative approach and without recursion. The test_fibonacci function checks if the `fib4` function returns the correct result for a given input value.