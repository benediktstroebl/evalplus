```python
def fibfib(n):
    # handle special cases
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    # otherwise, iterate through previous values and add them up
    return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```
This code defines a recursive function `fibfib` that follows the definition of the FibFib sequence provided in the prompt. It handles the base cases of `n=0`, `n=1`, and `n=2` separately, and for larger `n`, it recursively calls itself with the previous three elements in the sequence, adding them up to provide the `n`th element. 

Here are some examples of how this function behaves: 
```python
>>> fibfib(1)
0
>>> fibfib(5)
4
>>> fibfib(8)
24
```
These examples correspond to the test cases provided in the original prompt, and they illustrate the FibFib sequence as defined. 

This is a recursive approach to solving the problem, and as such, it may not be the most efficient for large values of `n` due to the overlapping computations of overlapping subproblems. For larger inputs, the function will eventually exceed the stack-size limit for recursive calls in Python, causing a `RecursionError`. However, the code passes the provided tests correctly for smaller values.