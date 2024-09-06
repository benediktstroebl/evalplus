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
    n = int(input("Enter a number to test the Fibonacci function: "))
    if n < 0:
        print("Please enter a positive number.")
    else:
        result = fib4(n)
        print(f"The {n}th Fibonacci number is {result}")

test_fib4()
```

This script defines a function called `fib4` that computes the nth Fibonacci number using a loop-specific approach. The `test_fib4` function prompts the user to enter a number, then calls `fib4` to compute and print the result.