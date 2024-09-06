Here is the updated Python script with self-contained function:

```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which the first two are 0 and 1, and each subsequent number is the sum of the previous two. The Fibonacci sequence is an efficient implementation using the naive method, which uses a loop to calculate the n-th element.
    if n <= 1:
        return 0
    elif n <= 3:
        return fib4(n - 1) + fib4(n - 2)
    else:
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3)

test_fib4 = fib4
test_fib4(5)
test_fib4(6)
test_fib4(7)
```

This code defines a function called fib4 that calculates the n-th element of the Fibonacci sequence. It uses a standard Fibonacci sequence, which starts with 0 and 1 and then adds the previous two numbers to get the next one. The function checks if the n is less than or equal to 1, in which case it returns 0. If n is greater than 1, it recursively calls itself to calculate the next element in the sequence.

The code then defines a function called test_fib4 that calls fib4 with the argument 5, 6, and 7, which are test cases for the function. This function returns the test the results of the function calls, which are the values of the Fibonacci sequence at the corresponding indices.