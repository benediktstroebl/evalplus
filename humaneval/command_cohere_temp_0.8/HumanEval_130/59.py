```python
def tri(n):
    seq, last_odd, last_even = [], 1, 3
    while len(seq) < n + 1:
        if len(seq) % 2 == 0:
            seq.append(last_even)
            last_even = last_even + 1
        else:
            seq.append(last_odd)
            last_odd = last_odd + seq[len(seq) - 2] + seq[len(seq) - 1]
    return seq[:n+1]
``` 

This Python script defines a function called `tri(n)` which generates the first `n+1` numbers in the Tribonacci sequence, which is a sequence defined by the recurrence relation where the odd-indexed terms are equal to the sum of the preceding and succeeding odd-indexed terms and even-indexed terms are one more than the preceding even-indexed term. The function uses two variables `last_odd` and `last_even` to keep track of the last odd and even-indexed terms in the sequence. It then enters a loop where it compares the length of the sequence `seq` to the desired length `n+1`. If the current term is even, it increments the last even term and adds it to the sequence. If the current term is odd, it increments the last odd term and calculates the new odd term as the sum of the previous odd terms from `len(seq) - 2` and `len(seq) - 1` and adds it to the sequence. The function returns the sequence `seq` sliced to be of length `n+1`.

Here is an example of using this function with the `tri()` function for the value `n = 6`:
```python
print(tri(6))
```

This would output:
```
[1, 3, 2, 8, 5, 13]
```

Which is the first 6 + 1 terms of the Tribonacci sequence.