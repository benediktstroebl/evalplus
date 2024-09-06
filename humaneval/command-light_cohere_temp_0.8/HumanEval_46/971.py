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

# Example usage:
print(fib4(5))  # Output:   14
``` 
This code defines a Python function `fib4` that computes the n-th Fibonacci number in the Fibonacci sequence using the recursive definition:

The function uses a base case for n equal to 0, which returns 0. For n equal to 1, it returns 0, as the first number in the sequence. For n equal to 2, it returns 2, as the second number in the sequence. For n equal to 3, it returns 0, as the third number in the sequence. For n greater than 4, it recursively computes the n-th Fibonacci number by summing the previous four numbers.