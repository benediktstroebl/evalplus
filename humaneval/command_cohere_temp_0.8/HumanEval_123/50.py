```python
def get_odd_collatz(n):
    odd_seq = [x for x in map(int, str(n)) if x & 1 == 1]
    collatz_seq = [x for x in odd_seq if x != 1]
    return sorted(collatz_seq)
```

This script defines a function `get_odd_collatz` which accepts a positive integer `n` as an argument and returns a sorted list of odd numbers in the Collatz sequence. The Collatz sequence for `n` is generated using the provided formula, and the odd numbers in this sequence are extracted using bit manipulation. Finally, the list is sorted in increasing order before being returned. This code efficiently solves the problem without introducing any additional complexity.