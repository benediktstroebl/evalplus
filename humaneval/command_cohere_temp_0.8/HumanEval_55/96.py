```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single integer argument n. This function is tasked with calculating the n-th Fibonacci number. The Fibonacci sequence is an series where each successive value is the sum of the two preceding ones, starting from 0 and 1.

The script employs a conditional statement to check if n is less than 2. If so, it returns n, acknowledging that the first two numbers in the Fibonacci sequence are 0 and 1. However, if n is not less than 2, the function recursively calls itself to calculate the sum of the (n-1)-th and (n-2)-th Fibonacci numbers and returns this sum.

This approach, while simple, can become inefficient for larger values of n due to the repeated recursive calculations of the same Fibonacci numbers. Nonetheless, the function duly fulfills the problem requirement of returning the n-th Fibonacci number as stipulated.

The script does not include any test cases, but the function is designed to be independently testable and validated. Sample test cases can be added to a separate module to thoroughly exercise the function and ensure its correctness across a range of inputs. These tests would encompass both edge cases and regular scenarios to comprehensively verify the function's behavior and outcomes.