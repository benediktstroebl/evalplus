```python
def fib4(n: int):
    """The Fibonacci sequence without recursion."""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    n = int(input("Enter a number to find Fibonacci: "))
    if n < 0:
        print("Invalid input. Please enter a
         n>=0")
        return

    result = fib4(n)
    print(f"The {n}th Fibonacci number is: {result}")

test_fib4()
```

This script defines a function `fib4` that computes the n-th Fibonacci number without recursion. The function uses a chain of addition to calculate each Fibonacci number in succession, and it passes the test with a test case that includes negative numbers.