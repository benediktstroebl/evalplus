```python
def fib4(n: int):
    prev = [0, 0, 2, 0]
    current = [0, 0, 0, 0]
    for i in range(n):
        next = [x + y for x, y in zip(current, prev)]
        prev, current = current, next
    return current[0]
```
This script uses an iterative approach to calculate the Fib4 number sequence for n-th terms larger than 4, avoiding recursion as per the prompt. It utilizes three arrays, prev, current, and next, to store the previous, current, and next terms in the sequence, updating these arrays accordingly. The result is returned as current[0], which will be the n-th Fib4 number.