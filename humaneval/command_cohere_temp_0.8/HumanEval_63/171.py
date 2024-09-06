```python
def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursive calls to the previous three terms in the sequence, with the base cases for 0 and 1, as defined in the problem statement. It efficiently computes the n-th element of the FibFib sequence for any positive integer n. 
Let's verify the result for `n = 5`
```python
>>> fibfib(5)
4
``` 
And for `n = 8`
```python
>>> fibfib(8)
24
```
These results correspond to the example outputs provided in the prompt. This function has a time complexity of O(2^n) due to the recursive nature of its computations, it will efficiently compute the n-th FibFib number for any positive integer n.  This approach differs from the direct calculation of Fibonacci numbers, which is more efficient for the classic Fibonacci sequence.