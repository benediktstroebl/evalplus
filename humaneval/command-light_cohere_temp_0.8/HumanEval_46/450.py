```python
def fib4(n: int):
    """The Fibonacci sequence without recursion.
    fib_seq = [0, 1]
    while n > 0:
        fib_seq.append(fib_seq[n-1] + fib_seq[n-2])
        n -= 1
    return fib_seq[-1]

# Test cases
test_fib4 = []

test_fib4.append([int](fib4(5))[0])
test_fib4.append(int)(fib4(6)[0])
test_fib4.append(int)(fib4(7)[0])

# Report the test results
print("Test results:")
for item in test_fib4:
    print(item, end=" ")
```
The function `fib4` computes the n-th element of the Fibonacci sequence without recursion. It uses an iterative approach and a list `fib_seq` to store the sequence. The function returns the final element of the sequence.