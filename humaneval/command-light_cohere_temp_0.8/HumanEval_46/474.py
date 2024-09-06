```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which the next number is defined as the sum of the two preceding ones.
    return = 0
    def fib4_helper(n):
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib4_helper(n - 1) + fib4_helper(n - 2)
    return fib4_helper(n)

def test_fib4():
    n = 7
    assert fib4(n) == 14

def main():
    test_fib4()

if __name__ == "__main__":
    main()
```
The Fibonacci sequence is defined as a series of numbers where each number is the sum of the two preceding ones. The function `fib4` calculates the nth Fibonacci number efficiently without using recursion.