```python
def get_odd_collatz(n):
    odd_seq = [x for x in collatz_sequence(n) if x % 2 != 0]
    return sorted(odd_seq)

def collatz_sequence(n):
    if n == 1:
        return [1]
    else:
        seq = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            seq.append(n)
        return seq
```

The `collatz_sequence` function directly implements the definition of the Collatz sequence, returning the sequence of integers starting from `n` and following the Collatz conjecture's rules. The `get_odd_collatz` function filters out even numbers from the Collatz sequence and sorts the result. Both functions are tested with the provided unit tests.  This code provides a efficient and concise implementation for the problem.