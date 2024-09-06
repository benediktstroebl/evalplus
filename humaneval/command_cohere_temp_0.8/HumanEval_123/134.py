Here's a Python script with a self-contained function `get_odd_collatz` that solves the problem:
```python
def get_odd_collatz(n):
    odd_seq = [3*i+1 for i in range(1, n+1, 2)]
    even_seq = [i//2 for i in range(n, 1, 2)]
    odd_seq.extend(even_seq)
    return odd_seq

# Test Cases
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(14) == [1, 7, 13]
```

This script defines a function `get_odd_collatz(n)` that returns the odd numbers in the Collatz sequence for a given positive integer `n`.

For odd `n`, the script directly generates the odd sequence of the Collatz sequence. It starts with `3*i+1`, where `i` starts from 1 and increments by 2 to ensure only odd numbers are generated.

For even `n`, the script generates the even sequence of the Collatz sequence, which is calculated by dividing each even number `n` in the sequence by 2. 

The odd and even sequences are then combined (the odd sequence is extended with the even sequence) to form the full Collatz sequence. This is done because the problem's statement explicitly asks for only odd numbers from the Collatz sequence.

The test cases provided in the problem statement are also included to validate the function's correctness. 

Please let me know if this solution satisfies your needs or if you would like me to make any adjustments to it.