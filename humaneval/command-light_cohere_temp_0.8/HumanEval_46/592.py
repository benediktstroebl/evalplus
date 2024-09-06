```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fibonacci sequence starts with 0 and 1, and the next number is the sum of the previous two numbers.
    return:
        if n < 0:
            raise ValueError("n should be a non-negative integer")
        elif n == 0 or n == 1:
            return 0
        elif n == 2:
            return 2
        else:
            a, b = 0, 1
            for _ in range(n - 2):
                a, b = b, a + b
            return b
    ```