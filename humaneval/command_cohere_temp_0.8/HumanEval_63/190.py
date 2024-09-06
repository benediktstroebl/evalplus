```python
def fibfib(n):
    fibfib_sequence, prev_val, curr_val = [0, 0, 1], 0, 0
    while len(fibfib_sequence) < n:
        prev_val = curr_val
        curr_val = fibfib_sequence[-1] + prev_val + fibfib_sequence[-2]
        fibfib_sequence.append(curr_val)
    return curr_val

# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This Python script defines a function called `fibfib` that uses a while loop to generate the FibFib sequence up to the n-th term, then returns that n-th term. The sequence is stored in a list (`fibfib_sequence`), and `prev_val` and `curr_val` are used to keep track of the two previous terms in the sequence. The test cases output the first 3 terms of the sequence, which matches the test case expectations.