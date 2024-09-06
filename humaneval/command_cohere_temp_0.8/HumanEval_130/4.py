```python
def tri(n):
    sequence, last_odd, last_even = [1], 1, 3
    while len(sequence) < n + 1:
        if len(sequence) % 2 == 0:
            sequence.append(last_even)
            last_even = last_even + last_odd + sequence[-1]
        else:
            sequence.append(sequence[-1] + sequence[-2] + last_odd)
            last_odd = last_odd + sequence[-1]
    return sequence[:n+1]
``` 

The problem asks us to generate the first `n + 1` terms of the Tribonacci sequence, which is defined as follows:
- `tri(1) = 3`
- `tri(n) = 1 + n / 2, if n is even`
- `tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd`

We approach the problem by defining two parallel arrays, `sequence` to store the generated numbers, and `last_odd, last_even` to store the last odd and even outputs respectively. Then, we use a `while` loop to generate the next terms in the sequence by adding the preceding terms till we have generated `n + 1` terms. Finally, we return the `sequence` array upto the length `n + 1`.