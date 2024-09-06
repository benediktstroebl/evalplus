```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. The function computes the n-th Fibonacci number recursively. The base cases are defined with the condition if n < 2, in which it returns n, as the first two numbers in the Fibonacci sequence are 0 and 1. If n is greater than or equal to 2, it returns the sum of the (n-1)th and (n-2)th Fibonacci numbers, which are the next two numbers in the sequence. This code will calculate the Fibonacci numbers correctly for any positive integer input n. 
```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Test cases
print(fib(10))  # Output: 55
print(fib(1))  # Output: 1
print(fib(8))  # Output: 21
```
You can incorporate this code snippet into your Python script, and you can modify the test cases to match your specific requirements.  This function will yield the correct Fibonacci numbers for any valid non-negative integer input.