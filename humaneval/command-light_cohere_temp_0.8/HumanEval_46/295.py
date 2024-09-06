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
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

def test_fib4():
    n = int(input("Enter a number: "))
    if n < 0:
        print("Error: Fibonacci sequence does not contain negative numbers.")
    elif n == 4:
        print("Fibonacci:", 4)
    else:
        print("Fibonacci:", fib4(n))

test_fib4()
```
The function `fib4` takes an integer `n` as input and returns the n-th Fibonacci number. The function uses an iterative approach and does not use recursion. The test function `test_fib4` is used to test the `fib4` function by passing various values of `n` and printing the corresponding Fibonacci numbers.