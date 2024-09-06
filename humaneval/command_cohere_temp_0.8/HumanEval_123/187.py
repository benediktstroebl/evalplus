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

The `collatz_sequence` function directly implements the definition of the Collatz sequence, returning the sequence of integers starting from `n` and following the Collatz rules. The `get_odd_collatz` function then filters out the odd numbers from this sequence and sorts them. This approach is efficient and relatively straightforward, ensuring the function's correctness.