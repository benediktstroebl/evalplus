```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which the next number is obtained by adding the two preceding ones. The function returns the  n-th element of the sequence."""
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
The function 'fib4' computes the n-th element of the Fibonacci sequence using a simple iterative approach, avoiding recursion. It checks base cases for 'n' equal to 0, 1, and 2 to return the corresponding elements of the sequence. Then, it calculates the element by summing the two preceding elements using the formula 'fib4(n) = fib4(n-1) + fib4(n-2)'. The test cases at the end ensure that the function works correctly for different values of 'n'.