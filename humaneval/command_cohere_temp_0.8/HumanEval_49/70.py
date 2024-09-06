Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return (1 << n) % p

# Tests
n, p = 3, 5
print(f"{n} modulo {p} = {modp(n, p)}")  # Should print 3

n, p = 1101, 101
print(f"{n} modulo {p} = {modp(n, p)}")  # Should print 2

n, p = 0, 101
print(f"{n} modulo {p} = {modp(n, p)}")  # Should print 1

n, p = 3, 11
print(f"{n} modulo {p} = {modp(n, p)}")  # Should print 8

n, p = 100, 101
print(f"{n} modulo {p} = {modp(n, p)}")  # Should print 1
```

This script defines the `modp` function that takes two integers `n` and `p` as input and returns `2^n % p`. It also includes tests that verify the function's behavior against various inputs. 

To run the tests, you would need to execute the script. You can do so by copying the script and pasting it into a Python interpreter or saving it as a .py file and running it using the command line: `python script.py`. 

The tests will then print out the calculated results of `n` modulo `p` with different input values, and since the expected output matches the printed results, this indicates that the function is correctly solving the problem.