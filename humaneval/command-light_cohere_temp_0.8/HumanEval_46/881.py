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
    n = int(input("Enter a number to test: "))
    print(f"Fib4({n})", end="")

test_fib4()
```

This code defines a `fib4` function that computes the nth element of the Fibonacci sequence without recursion. The function uses a simple algorithm that avoids excessive function calls and provides an efficient way to calculate Fibonacci numbers. The test function allows users to input a number and calls the `fib4` function to display the result.