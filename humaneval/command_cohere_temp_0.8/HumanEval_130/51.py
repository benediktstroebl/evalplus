```python
def tri(n):
    seq, last_odd, last_even = [], 1, 3
    for i in range(n + 1):
        if i % 2 == 0:
            seq.append(last_even)
            last_even = 1 + i / 2
        else:
            seq.append(last_odd)
            last_odd = seq[i - 1] + seq[i - 2] + last_even
    return seq
``` 

This Python script defines a function called `tri(n)` which calculates the Tribonacci sequence for the first `n+1` numbers. The function uses two variables, `seq` and `last_odd`, to keep track of the sequence and the last odd Tribonacci number, respectively. The first two elements of the sequence are initialized to 1 and 3.

The function then enters a loop that runs `n+1` times. Within the loop, it checks whether the current index `i` is even or odd. If `i` is even, it calculates the next Tribonacci number by summing the previous even number and the average of the two previous odd numbers. The `seq` list is then appended with this new even Tribonacci number. Subsequently, the `last_even` variable is updated to the value of the newly calculated even number.

If `i` is odd, the function appends the previous odd Tribonacci number to the `seq` list. It then updates the `last_odd` variable to the value of the sum of the two previous odd numbers plus the previous even number.

After the loop completes, the function returns the `seq` list, which contains the first `n+1` numbers of the Tribonacci sequence. This approach efficiently calculates the Tribonacci sequence while ensuring sequential consistency.