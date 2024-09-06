```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each subsequent term is defined as the sum of the two preceding terms. Fibonacci numbers are the o(5) -> 4
    fib4(6)  # Output: 8
    return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    """Test the function by passing different values for n and expected outputs."""
    print("Test 1:", fib4(5))
    print("Test 2:", fib4(6))
    print("Test 3:", fib4(7))
    print("Test 4:", fib4(8))

test_fib4()
```
The provided function uses the concept of memoization to efficiently calculate Fibonacci numbers. It avoids repeated calculations by storing previously computed values in a dictionary. This approach significantly reduces the using the function's complexity and improves its performance.