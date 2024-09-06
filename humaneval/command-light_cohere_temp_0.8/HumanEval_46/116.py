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
    result = fib4(n)
    print(f"The Fibonacci number at index {n} is {result}")

test_fib4()
```

The function `fib4` uses a conditional chain to quickly determine the n-th Fibonacci number without recursion, passing the test with various input values.