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

The code defines a function 'tri()' which returns the Tribonacci sequence of numbers for `n+1` where `n` is the input to the function. It initializes an empty `list` called `seq` to store the sequence and two variables `last_odd` and `last_even` to keep track of the last odd and even Tribonacci numbers. The function goes through iterations using a `for` loop to calculate and store the Tribonacci numbers in `seq` correctly based on the definition of the Tribonacci sequence for each number from 1 to `n`. It checks if the iteration is even using the `% 2 == 0` condition, then it calculates the even Tribonacci number using the formula `1 + i / 2` and updates `last_even`. Otherwise, it calculates the odd Tribonacci number by summing the last two odd Tribonacci numbers and updates `last_odd`. The output of the function is the list `seq`, which contains the first `n + 1` numbers of the Tribonacci sequence.