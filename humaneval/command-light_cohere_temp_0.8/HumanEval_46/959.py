```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each successive term is defined as a ratio of the previous two terms. The sequence begins with the 0 and 1, and the subsequent terms are the sum of the two preceding ones."""
    return (0, 1)

for _ in range(5):
    n = _ + 1
    result = fib4(n)
    print(f"n: {n}, result:{result}")
```