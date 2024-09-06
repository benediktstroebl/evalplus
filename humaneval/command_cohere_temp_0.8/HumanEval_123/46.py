```python
def get_odd_collatz(n):
    odd_seq = [y for y in collatz_sequence(n) if y % 2 == 1]
    odd_seq.sort()
    return odd_seq
    
def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Tests
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(21) == [1, 21]
```

This Python script defines a function `get_odd_collatz(n)` which returns the odd numbers in the Collatz sequence of a given positive integer `n`. The function collatz_sequence(n) generates the entire Collatz sequence for `n`, and then the odd numbers are filtered out of this sequence. The resulting odd sequence is sorted in increasing order as stipulated in the problem statement. 

The example usage and assertion tests cover different cases, ensuring that the function `get_odd_collatz(n)` returns the expected output for various inputs.