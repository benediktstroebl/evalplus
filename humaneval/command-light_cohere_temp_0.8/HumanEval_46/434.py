```python
def fib4(n: int):
    """The Fibonacci sequence without recursion. The formula used by Binet driver is:
        return (fib4(n-1) + fib4(n-2)) + fib4(n-3) + fib4(n-4)

def test_fib4():
    n = int(input("Enter a number: ":"))
    result = fib4(n)
    print(f"The Fibonacci number for n={n} is: {result}")

test_fib4()
```

This code defines a `fib4` function that computes the n-th Fibonacci number without recursion. The `test_fib4` function takes user input for a number and passes it to the `fib4` function to compute the corresponding Fibonacci number. The result is then printed to the console.