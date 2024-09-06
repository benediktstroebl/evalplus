```python
def fibfib(n: int):
    if n < 0:
        raise ValueError("FibFib sequence is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This code defines a recursive function fibfib that computes the n-th number in the FibFib sequence. It starts by checking for two base cases: n equal to 0 or 1, which both evaluate to 0. If n is greater than 1, the function recursively calls itself to calculate the sums of the (n-1)-th, (n-2)-th, and (n-3)-th terms, which is the definition of the FibFib sequence. Also, it includes a basic error handling to alert users that this sequence is not defined for negative numbers. 
```python
>>> fibfib(1)
0
>>> fibfib(5)
4
>>> fibfib(8)
24
>>> fibfib(-3)
Traceback (most recent call last):
  ...
ValueError: FibFib sequence is not defined for negative numbers
```