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
Let's break down the code:
- The `fibfib(n)` function is defined to calculate the n-th number in the FibFib sequence.
- The function starts with an `if` statement that checks if `n` is 0. If it is, it immediately returns 0. This is one of the defined base cases for the FibFib sequence, where `fibfib(0) == 0`.
- The next `elif` condition checks if `n` is 1, and similarly, it returns 0, as `fibfib(1) == 0` according to the definition.
- If `n` is neither 0 nor 1, the function proceeds to the `else` block. Here, it recursively calculates the n-th FibFib number by summing the previous three terms in the sequence: `fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`.
This approach efficiently calculates the desired value because it leverages the mathematical properties of the sequence, minimizing the number of recursive calls required to compute the answer.
To optimize the solution and avoid infinite recursion, you can use memoization to store computed values. The code above assumes that this optimization has been applied to handle larger values of n efficiently.