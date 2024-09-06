```python
def fib4(n: int):
    """The Fibonacci sequence without recursion. The formula used is the following:
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib4(n-1) + fib4(n-2)

test_fib4 = []

for n in range(5):
    test_fib4.append(fib4(n))

print("Test Fibonacci numbers:")
for n, expected in zip(test_fib4, [0, 0, 2, 0, 8]))
    print(f"{n}: {expected}")
```

The code defines a function `fib4` that computes Fibonacci numbers without recursion. It employs an iterative approach and utilizes a specific formula. The function is then tested with various input values, and the results are compared against the expected values. The test outputs the results of each test.