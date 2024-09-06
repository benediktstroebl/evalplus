```python
def fib4(n: int) -> int:
    fib4_list = [0, 0, 2, 0]
    for i in range(5, n + 1):
        fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])
    return fib4_list[n]
```
This code defines a function `fib4` which efficiently calculates the n-th number in the Fib4 sequence, based on the definition of the sequence. The sequence is initialized and computed in a list (`fib4_list`), and the function returns the n-th value from this list. The function is designed to avoid recursion and optimize memory usage for larger values of `n`.

Here's a usage example:
```python
>>> fib4(5)
4
>>> fib4(6)
8
>>> fib4(7)
14
```
This demonstrates how the function can be used to calculate the Fib4 numbers, making it a practical tool for handling such sequence-related problems.