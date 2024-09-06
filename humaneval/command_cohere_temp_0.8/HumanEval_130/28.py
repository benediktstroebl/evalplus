```python
def tri(n):
    Sequence = [1, 3]
    if n >= 1:
        Sequence.extend(Sequence[-2:] + [Sequence[-1] + Sequence[-2] + x for x in Sequence[1:-2]] + [Sequence[-1]])
    return Sequence[:n+1]
``` 

The code defines a recursive function `tri(n)` that generates the `n+1` first numbers of the Tribonacci sequence. It starts with initializing the sequence with the first two elements (1 and 3), and then recursively computes the subsequent elements based on the recurrence relation, `tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1)`, alternating between even and odd indices. The generated sequence is stored in the `Sequence` list and is returned sliced to provide the first `n+1` numbers of the Tribonacci sequence.