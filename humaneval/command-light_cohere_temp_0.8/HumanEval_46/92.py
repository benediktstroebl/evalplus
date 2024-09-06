```python
def fib4(n: int):
    """The Fibonacci sequence without recursion.
    a = [0, 1]
    while n > 0:
        a, b = a+b, a
        n -= 1
        yield a
```

This Python function generates the nth element in the Fibonacci sequence without recursion. It uses an iterative approach with two variables `a` and `b` that are added and subtracted to each other, producing the next Fibonacci number. The function starts with the initial values of `a` and `b` set to `0` and `1`, respectively. It then enters a `while n > 0:` loop, where `n` is decremented and the next Fibonacci number `a` is yielded. The loop continues until `n` becomes 0, and the entire Fibonacci sequence is generated. 

This function is self-contained and efficient, providing a straightforward way to generate the Fibonacci sequence without recursion.