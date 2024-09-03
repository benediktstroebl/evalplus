```python
def f(n):
    """ Returns a list of size n with the element at index i being the factorial of i if i is even,
    or the sum of numbers from 1 to i if i is odd.
    """
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum(range(1, i + 1)))
    return result

def factorial(n):
    """Returns the factorial of n."""
    if n == 0:
        return 1
    return n * factorial(n - 1)
```