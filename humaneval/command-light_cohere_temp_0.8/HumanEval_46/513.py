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

# Example usage
print(fib4(5))
print(fib4(6))
print(fib4(7))
```

The code defines a function called fib4 that takes an integer n as input and returns the n-th Fibonacci number in the sequence. The function uses a following approach:
1. Define a base case for n equal to 0, 1, and 2, where the Fibonacci numbers are 0, 0, and 2, respectively.
2. For n greater than start with the code block that calls the function again with n-1, n-2, n-3, and n-4, respectively.
3. The function is called recursively until it reaches the base case or until the value of n is less than 5.

The function uses a simple mathematical calculation to compute the n-th Fibonacci number in the sequence, and it does not use any complex libraries or recursive functions. The output of the function is the n-th Fibonacci number in the sequence.