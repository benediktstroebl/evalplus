```python
def tri(n):
    sequence, last_odd, last_even = [], 1, 3
    while len(sequence) < n + 1:
        if len(sequence) % 2 == 0:
            sequence.append(last_even)
            last_even = last_even + last_odd + next_odd
            last_odd, next_odd = last_odd + 1, last_odd + 2
        else:
            sequence.append(last_odd)
            last_odd = last_odd + last_even + next_even
            last_even, next_even = last_even + 1, last_even + 2
    return sequence
```

The code defines a function 'tri()' which generates the Tribonacci sequence of numbers up to the n-th term, it uses two "pointers" (`last_even` and `last_odd`) which point to the last generated even and odd terms in the sequence. Then, in a loop, the code checks whether the next term to be added is even or odd, updating the appropriate pointer(s) and adding the necessary values to generate the next term, it ensures that the sequence is padded with the necessary number of zeros, so that `len(sequence) >= n + 1`.