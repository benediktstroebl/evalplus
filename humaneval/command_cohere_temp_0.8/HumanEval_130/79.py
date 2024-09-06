```python
def tribonacci(n):
    sequence = [0, 0, 0]
    for i in range(n+1):
        if i == 1 or i % 2 == 0:
            sequence.append(3)
        else:
            sequence.append(sequence[i-1] + sequence[i-2] + sequence[i+1])
    return sequence
```
This Python script defines a function called `tribonacci` that generates the Tribonacci sequence up to a given index `n`. The sequence is initialized with three zeros, and then it iteratively computes the subsequent terms based on the recurrence relation. If `i` is 1 or even, it appends 3 to the sequence. If `i` is odd, it computes the sum of the previous three terms and appends it to the sequence. The function returns the list of the first `n+1` terms of the Tribonacci sequence.