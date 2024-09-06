```python
def tri(n):
    seq, last_odd, last_even = [], 1, 3
    while len(seq) < n + 1:
        if len(seq) % 2 == 0:
            seq.append(last_even)
            last_even = 1 + last_even // 2
        else:
            seq.append(sum(seq[-2:]))
            last_odd = last_odd + last_even + 1
            last_even = seq[-1]
    return seq[:n+1]
``` 

The problem asks us to generate the first `n + 1` terms of the Tribonacci sequence, which is defined as follows:
- `tri(1) = 3`
- `tri(n) = 1 + n / 2, if n is even`
- `tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd`

We use a while loop to generate the sequence, appending values to `seq` array as follows:
- If the length of the sequence is even, we append the value of `last_even` which is updated after each iteration to the next value in the sequence (`1 + last_even // 2`).
- If the length of the sequence is odd, we calculate the next value in the sequence by summing the last three values in the sequence (`sum(seq[-2:])`), as defined by the recurrence.

The loop continues until the length of the sequence is greater than `n`, and then we return the first `n + 1` values of the sequence, as requested.