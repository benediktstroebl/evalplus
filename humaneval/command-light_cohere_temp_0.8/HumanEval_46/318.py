```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fib4 sequence is defined as follows:
    fib4(0) = 0
    fib4(1) = 0
    fib4(2) = 2
    fib4(3) = 0
    fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    return fib4

def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

def main():
    if __name__ == '__main__':
        test_fib4()

```

The script defines a function `fib4` that computes the n-th Fibonacci number using the recursive formula: `fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)`. It then defines a function `test_fib4` to conduct various tests, such as the result for the value of `fib4(5)` and `fib4(6)`. 

The `main` function is then executed, which serves as the entry point of the script and runs the `test_fib4` function to verify the correctness of the `fib4` function.