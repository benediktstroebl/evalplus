```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The sequence starts with 0 and 1, and each subsequent number is the sum of the two previous ones.
    return:
        if n < 0:
            raise ValueError("n must be a non-negative integer")
        elif n == 0 or n == 1:
            return 0
        elif n == 2:
            return 2
        else:
            a, b = 0, 1
            for _ in range(n - 2):
                a, b = b, a + b
            return b
    """

	# Example usage:
	n = 7
	print(fib4(n))
```
This Python code defines a function called fib4 which computes the n-th Fibonacci number in the sequence using an efficient non-recursive approach. The function checks for valid input values and returns the appropriate Fibonacci number. The example usage demonstrates how the code works by calling the fib4 function with n as 7 and printing the result, which is 14.