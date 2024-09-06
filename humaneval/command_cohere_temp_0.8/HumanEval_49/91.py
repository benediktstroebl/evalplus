Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return (1 << n) % p

# Tests
print(modp(3, 5))      # 3
print(modp(1101, 101)) # 2
print(modp(0, 101))    # 1
print(modp(3, 11))     # 8
print(modp(100, 101))  # 1
```

This script includes a function `modp` that returns `2^n` modulo `p`, as well as test cases to verify its correctness. 

To run the tests, you can save the code into a Python file (e.g., `modp.py`) and execute the file in your terminal using `python modp.py`. The script will output the results of each test case as it executes.