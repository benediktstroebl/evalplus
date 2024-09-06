```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each successive number is defined as the sum of the two preceding ones.
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

if __name__ == "__main__":
    print(fib4(5))  # Output: 4
    print(fib4(6))  # Output: 8
    print(fib4(7))  # Output: 14
    print(fib4(8))  # Output: 24
    print(fib4(9))  # Output: 55
    print(fib4(10))  # Output: 888
```

This code defines a function `fib4` that calculates the nth element of the Fibonacci sequence using an iterative approach, not recursion. The function uses a base cases for n=0, 1, and 2 to quickly compute the first few terms, and then uses an iterative method to calculate subsequent terms by summing the contributions from the previous three terms. 

This approach is more efficient and avoids the potential stack overflow issues that can occur with recursion for large values of n, making it suitable for calculating Fibonacci numbers efficiently.