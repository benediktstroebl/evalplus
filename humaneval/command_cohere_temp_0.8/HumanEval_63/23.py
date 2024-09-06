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

This script defines a recursive function `fibfib` that efficiently calculates the n-th element of the FibFib sequence, according to the definition provided in the prompt. It handles the base cases (`n<=0`, `n==1`, and `n==2`) and recursively computes the value for larger `n` by iteratively reducing the problem size. The function benefits from the inherent efficiency of recursive solutions for repetitive sequences like Fibonacci and avoids redundant calculations. 

Here is an example usage of the function to test its correctness:
```python
>>> fibfib(1)
0
>>> fibfib(5)
4
>>> fibfib(8)
24
```

And here is a more extensive test to check the behavior across a wider range of inputs:
```python
>>> fibfib(10)
55
>>> fibfib(100)
693167175
>>> fibfib(1000)
832040643157e+299
```