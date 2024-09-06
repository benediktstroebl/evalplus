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

This Python script defines a function called `tri(n)` that generates the first `n+1` numbers in the Tribonacci sequence, which is a sequence similar to the Fibonacci sequence but with different recurrence relations for odd and even indices. 

The function starts by initializing an empty sequence `seq` to store the Tribonacci numbers and assigns `last_odd` and `last_even` values to 1 and 3, respectively, as these are the first odd and even Tribonacci numbers. 

Then, it enters a loop that continues generating Tribonacci numbers until the length of the sequence is greater than `n`, using the following logic: 

1. In each iteration of the loop, it checks whether the index is even or odd by checking the modulus of the length of the sequence by 2. 

2. If the index is even, it appends the current `last_even` value to the sequence and updates `last_even` to the sum of its previous value, the last odd Tribonacci number, and the current last even Tribonacci number. 

3. If the index is odd, it appends the sum of the last two odd Tribonacci numbers and the current last odd Tribonacci number to the sequence and updates `last_odd` to the sum of its previous value and the current last odd Tribonacci number. 

Finally, the function returns the first `n+1` numbers of the Tribonacci sequence as requested. 

This approach efficiently generates the Tribonacci sequence on the fly without the need for explicit recursion or memoization, making it both efficient and easy to understand.