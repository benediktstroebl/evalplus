```python
def fib4(n: int):
    """The Fibonacci sequence without recursion.
    a = [0, 1]
    for _ in range(n):
        a, b = a + a, b + b
    return a

# Test case
test_fib4 = []
for i in range(5):
    test_fib4.append(fib4(i))

# Output:
print('\n'.join(test_fib4))
```