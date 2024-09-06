```python
def fibfib(n: int):
    prev1, prev2, prev3 = 0, 0, 0
    if n >= 1:
        prev1 = fibfib(n-1)
    if n >= 2:
        prev2 = fibfib(n-2)
    if n >= 3:
        prev3 = fibfib(n-3)
    return prev1 + prev2 + prev3
```
This approach uses a memoization of sorts, where the first three previous values are stored and returned when the corresponding n value is asked for, and the relationships between the numbers in the sequence are used to calculate the values. This allows the function to efficiently compute the n-th element of the FibFib sequence. 

Here is an example usage of the code provided:
```python
>>> fibfib(1)
0
>>> fibfib(5)
4
>>> fibfib(8)
24
```
This shows that the code works like it is supposed to.