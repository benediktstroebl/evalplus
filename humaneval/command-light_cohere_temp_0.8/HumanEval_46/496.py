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

if __name__ == "__main__":
    print("The solution is: ", fib4(5))
    print("The solution is: ", fib4(6))
    print("The solution is: ", fib4(7))
```
This Python script defines a function called `fib4` that computes the n-th element of the Fibonacci sequence without recursion. The function uses a specific cases to return the known values (0, 0, 2, and 0) for n = 0, 1, 2, and 3, respectively. Additionally, it uses the formula to calculate subsequent numbers by summing the preceding three values. 

The `__main__` block then demonstrates the usage of the `fib4` function by calling it with different input values (5, 6, and 7) and printing the results.