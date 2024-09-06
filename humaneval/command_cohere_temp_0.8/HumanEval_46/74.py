```python
def fib4(n: int):
    prev = [0, 0, 2, 0]
    current = [0, 0, 0, 0]
    for i in range(n):
        next = [prev[j] + current[j] for j in range(4)]
        prev, current = current, next
    return current[0]
```
This code defines a function `fib4` that uses an iterative approach to calculate the nth number in the Fib4 sequence, fulfilling the problem statement's requirements. It transitions between three arrays (`prev`, `current`, `next`) to efficiently compute the values. This avoids the recursion called for in the tip. It is a self-contained solution that allows the calculation of Fib4 numbers without resorting to global variables or expensive recursion.