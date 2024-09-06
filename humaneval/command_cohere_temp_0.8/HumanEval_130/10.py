```python
def tri(n):
    sequences, last = [1], 3
    for _ in range(n):
        if _ % 2 == 0:
            sequences.append(last / 2 + 1)
        else:
            sequences.append(sequences[-1] + sequences[-2] + last)
        last = sequences[-1]
    return sequences
```
This Python script defines a function called 'tri' that generates the Tribonacci sequence by iterating through a given number of steps as determined by the input 'n' (with an extra iteration to include the last number in the sequence). The function produces a list of numbers that constitute the first 'n' plus one numbers of the Tribonacci sequence, which is then returned. The logic behind this sequence involves checking if the current step is even or odd; if it's even, it calculates the next number as '1 + n/2,' whereas if it's odd, it computes the next number as the sum of the previous three steps. This approach efficiently generates the requested Tribonacci sequence.