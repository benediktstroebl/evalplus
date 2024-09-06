Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return (1 << n) % p

# Tests
n, p = 3, 5
print(f"{n} % {p} = {modp(n, p)}")  # Should print 3

n, p = 1101, 101
print(f"{n} % {p} = {modp(n, p)}")  # Should print 2

n, p = 0, 101
print(f"{n} % {p} = {modp(n, p)}")  # Should print 1

n, p = 3, 11
print(f"{n} % {p} = {modp(n, p)}")  # Should print 8

n, p = 100, 101
print(f"{n} % {p} = {modp(n, p)}")  # Should print 1
```

This script defines the `modp` function that takes two integers `n` and `p` as arguments and returns `2^n % p`. It also includes tests that demonstrate the behavior of the function with different inputs. 

To run the tests, you would need to execute the script. You can do so by copying the code into a Python environment or IDE, or by saving it as a `.py` file and running it using the command line: 
```bash
python script.py
``` 

The tests will then print the computed results accordingly.