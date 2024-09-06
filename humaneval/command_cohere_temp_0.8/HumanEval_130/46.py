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
- `tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd`

We approach this sequentially:
1. We initialize an empty sequence `seq` to store our generated numbers, and seed the first two values as `last_odd` and `last_even` values.
2. We enter a `while` loop that continues until the length of `seq` is greater than `n`, ensuring that we have generated at least `n + 1` numbers.
3. Inside the loop, we check if the length of `seq` is even. If it is, we calculate the next value as the sum of the previous even value, `last_even`, and the last odd value, `last_odd`, and append it to `seq`. We then update `last_even` and `last_odd` accordingly.
4. If the length of `seq` is odd, we calculate the next value as the sum of the previous three values (`seq[-1] + seq[-2] + last_odd`), and append it to `seq`. We then update `last_odd` with the new value.
5. The loop continues until we have generated `n + 1` numbers.
6. Finally, we return the first `n` values of `seq`, ensuring that we have the complete Tribonacci sequence up to the `n-th` number. 

This approach efficiently generates the Tribonacci sequence as required.