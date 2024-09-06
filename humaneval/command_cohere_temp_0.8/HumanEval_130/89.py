```python
def tri(n):
    seq, last_odd, last_even = [], 1, 3
    while len(seq) < n + 1:
        if len(seq) % 2 == 0:
            seq.append(last_even)
            last_even = last_even + last_odd + seq[-1]
        else:
            seq.append(seq[-1] + seq[-2] + last_odd)
            last_odd = last_odd + seq[-1]
    return seq[:n+1]
``` 

The problem asks us to generate the first `n + 1` numbers in the Tribonacci sequence, which is defined as follows:
- `tri(1) = 3`
- `tri(n) = 1 + n / 2, if n is even`
- `tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd`

We approach this sequentially:
1. We initialize an empty list `seq` to store the sequence and initialize two variables `last_odd` and `last_even` with values 1 and 3 respectively.
2. We start a `while` loop that continues until the length of `seq` is greater than `n`, meaning we have generated all the required numbers.
3. We check if the length of `seq` is even. If it is, we append `last_even` to `seq` and update `last_even` to the sum of the previous odd number, current `last_even`, and the number just appended (`last_even = last_even + last_odd + seq[-1]`).
4. If the length of `seq` is odd, we append the sum of the last two elements of `seq` and the `last_odd` value to `seq` and update `last_odd` to the sum of the previous odd number and the number just appended (`last_odd = last_odd + seq[-1]`).
5. The loop continues until we have generated all the required numbers.
6. We return the first `n + 1` numbers in the Tribonacci sequence by taking a slice of `seq` from the beginning (`[:n+1]`).

The script above solves the problem by following these steps and will generate the required Tribonacci sequence for any `n` input into the `tri` function.