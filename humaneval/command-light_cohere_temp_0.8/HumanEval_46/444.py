```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2)

test_fib4 = []
for i in range(0, 8):
    test_fib4.append(fib4(i))

print("Test fib4 function results:")
for x in test_fib4:
    print(x, end=' ')
```