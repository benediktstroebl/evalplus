```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2)

# Example usage
print(fib4(5))
print(fib4(6))
print(fib4(7))
``` 
This code defines a function called fib4 that takes an integer n as input and returns the n-th Fibonacci number in the sequence. The function uses a simple formula to calculate the n-th Fibonacci number by summing the previous two numbers in the sequence.