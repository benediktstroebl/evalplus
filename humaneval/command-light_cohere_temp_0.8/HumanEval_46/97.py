```python
def fib4(n: int):
    if n <= 0:
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
    assert fib4(n) == 14

def main():
    test_fib4()

if __name__ == "__main__":
    main()
```
The function `fib4` calculates the nth element of the Fibonacci sequence using a loop-the Fibonacci sequence is a series of numbers where the next number is the sum of the two preceding numbers. 

You can test this function by calling `test_fib4` and passing the argument `n=7`, which should output `14`.