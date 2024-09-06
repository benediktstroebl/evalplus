```python
def tri(n):
    seq, last_odd, last_even = [], 1, 3
    for i in range(n + 1):
        if i % 2 == 0:
            seq.append(last_even)
            last_even = last_even + 1
        else:
            seq.append(last_odd)
            last_odd = last_odd + last_even + seq[i - 2]
    return seq
```

This Python script defines a function called `tri(n)` that calculates the Tribonacci sequence for the first `n+1` numbers. The function utilizes two variables, `last_even` and `last_odd`, to keep track of the last even and odd-indexed Tribonacci numbers, respectively. It initializes the sequence as an empty list and sets `last_even` to 1 and `last_odd` to 3, which are the initial values of the Tribonacci sequence.

The function then enters a loop that iterates from 1 to `n + 1`. Within the loop, it checks whether the current index `i` is even or odd using the modulo operator (`i % 2`). If `i` is even, it means we're dealing with an even-indexed Tribonacci number, so the function appends the current value of `last_even` to the sequence and updates `last_even` to the next Tribonacci number, which is simply one more than the previous value.

Conversely, if `i` is odd, it's an odd-indexed Tribonacci number, and the function appends the current value of `last_odd` to the sequence and updates `last_odd` to the next Tribonacci number, which is calculated by summing the previous `last_odd`, `last_even`, and the second-to-last odd-indexed Tribonacci number in the sequence.

This process continues for each value of `i` in the range, effectively building the Tribonacci sequence and returning it as a list from the `tri(n)` function.