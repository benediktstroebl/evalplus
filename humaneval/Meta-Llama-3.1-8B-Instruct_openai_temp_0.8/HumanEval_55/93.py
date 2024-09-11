### Fibonacci Number Generator
#### Fibonacci Series
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. In this example, we will use 1 and 1 as our starting numbers.

#### Code
```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to return.

    Returns:
    int: The n-th Fibonacci number.

    Examples:
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        fib_sequence = [1, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]

# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

#### Explanation
This script implements a recursive solution to the Fibonacci sequence problem. However, in this case we've used a loop instead for performance reasons, especially for larger inputs. The function starts with initializing a list with the first two Fibonacci numbers (1 and 1). It then enters a while loop, where it continues to append the sum of the last two numbers in the list until the list contains the desired number of Fibonacci numbers. The function then returns the last number in the list, which corresponds to the n-th Fibonacci number.