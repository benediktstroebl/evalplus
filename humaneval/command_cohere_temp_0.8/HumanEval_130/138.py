```python
def tri(n):
    seq, last_odd, last_even = [], 1, 3
    for i in range(n+1):
        if i % 2 == 0:
            seq.append(last_even)
            last_even = 1 + i / 2
        else:
            seq.append(last_odd)
            last_odd = seq[i-1] + seq[i-2] + last_even
    return seq
```
The Python script defines a function 'tri(n)' that generates the first 'n+1' terms of the Tribonacci sequence, which is a sequence similar to the Fibonacci sequence but with recursive relationships between odd and even indexed elements. It initializes an empty sequence 'seq' and two variables 'last_odd' and 'last_even' to represent the last odd and even-indexed Tribonacci numbers. The function iterates through 'n+1', calculating even-indexed terms as '1 + (i/2)', and odd-indexed terms as the sum of the previous three odd-indexed Tribonacci numbers. The result is a list 'seq' containing the first 'n+1' numbers of the Tribonacci sequence, which is then returned.