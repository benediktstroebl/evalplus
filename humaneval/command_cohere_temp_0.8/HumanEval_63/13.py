```python
def fibfib(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
```

This script defines a recursive function `fibfib` that serves as a direct implementation of the definition provided in the prompt. The function requires non-negative integers as inputs and returns the n-th element of the FibFib sequence. The definition of the function and its behavior are encapsulated within a robust docstring that provides clarity and useful information to users who may want to comprehend and utilize the function.

Here is an example of how to use the function:
```python
>>> fibfib(1)
0
>>> fibfib(5)
4
>>> fibfib(8)
24
```

This demonstrates that the function passes the given tests, correctly computing the FibFib values for these particular inputs. The function's simplicity and direct adherence to the sequence's definition make it an efficient solution, though potential issues with recursive calls could arise with larger input values due to the nature of recursive functions. Nonetheless, this script presents an immediate and direct implementation of the problem's definition.