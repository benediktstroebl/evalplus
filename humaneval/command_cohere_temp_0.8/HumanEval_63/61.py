```python
def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This function uses recursive calls to the previous three terms in the sequence, with the base cases for 0 and 1. 

Here is a more detailed breakdown of the function:
* The function takes an integer n as input, where n is the position of the desired FibFib number in the sequence.
* If n is 0, it returns 0 because the 0th element of the FibFib sequence is 0.
* If n is 1, it also returns 0 since the 1st element of the FibFib sequence is 0.
* For any other value of n, it recursively calls itself to calculate the last three terms of the sequence using the definition fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

The recursive approach makes efficient use of memory by storing only the necessary intermediate values and avoids repeated calculations by reusing previously computed results.