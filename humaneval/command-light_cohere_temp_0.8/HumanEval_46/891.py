```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers. The Fibonacci sequence can not be calculated using recursion, but can be calculated using a formula.
    return: The n-th Fibonacci number of the sequence as the sum of the previous two numbers.
    """
    sum(range(n - 1), (n - 1) * (n - 2) + (n - 3) * (n - 4))
    return n

# Driver code
n = int(input("Enter the value of n: "))
if n < 0:
    print("Please enter a positive integer.")
else:
    print("The Fibonacci number is", fib4(n))
```