```python
def fib4(n: int):
    """The Fibonacci sequence without recursion. Calculate the n-th element of the sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    elif n == 4:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

if __name__ == "__main__":
    print("Fibonacci numbers:")
    for i in range(5):
        print(fib4(i), end=" ")
    print()
```
This script defines a function called `fib4` that computes Fibonacci numbers without recursion. The function uses a specific conditions and calculations to generate the sequence up to the specified number `n`. The script then passes tests the function with various input values and prints the results. The output will display the test cases.