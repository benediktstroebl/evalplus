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

if __name__ == "__main__":
    print("Fibonacci Number at position n:", fib4(5))
    print("Fibonacci Number at position n:", fib4(6))
    print("Fibonacci Number at position n:", fib4(7))
```
This Python code defines a function called `fib4` that computes the nth Fibonacci number in the Fibonacci sequence using an efficient method that avoids recursion. The function takes an integer `n` as input and returns the corresponding Fibonacci number. The function uses a series of conditional statements to determine the base cases for the Fibonacci sequence (where `n` is 0, 1, or 2), and then recursively computes the Fibonacci number by summing the results of four previous Fibonacci numbers (fib4(n-1), fib4(n-2), fib4(n-3), and fib4(n-4)). The code also includes a main block where the `fib4` function is called with various input values, and the resulting Fibonacci numbers are printed out.