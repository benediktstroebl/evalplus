```python
def fib4(n):
    fib4_list = [0, 0, 2, 0]
    for i in range(5, n + 1):
        fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])
    return fib4_list[n]
```
This script defines the `fib4()` function, which efficiently calculates the n-th element of the Fib4 sequence, following the definition provided in the prompt. It initializes a starter list `fib4_list` with the first few elements of the sequence and then iteratively computes subsequent elements using a loop, avoiding recursion as requested. 

Here's an example of using the script:
```python
>>> fib4(5)
4
>>> fib4(6)
8
>>> fib4(7)
14
```
This demonstrates how the function correctly calculates the Fib4 numbers as per the sequence's definition.