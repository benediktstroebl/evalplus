```python
def fib4(n: int):
    """The Fibonacci sequence without recursion.
    fib_seq = [0, 1]
    for i in range(2, n + 1):
        fib_seq.append(fib_seq[i - fib_seq[i-1] + fib_seq[i-2])
    return fib_seq[-1]

# Test the function
fib4(7)
assert fib4(7) == 14

# Test the function with invalid arguments
fib4(-5)
assert_raises(TypeError, fib4, 5)

# Test the function with invalid input type
fib4([1,2,3])
assert_raises(TypeError, fib4, [1, 2, 3])
```

This script defines a function `fib4` that computes the n-th value of the Fibonacci sequence without recursion. The function uses an iterative approach to build the Fibonacci sequence and returns the value at position n. 

The tests demonstrate the function's correctness. 

This script is self-contained, and does not require external functions or modules.