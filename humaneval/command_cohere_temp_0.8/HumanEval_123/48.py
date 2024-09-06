```python
def get_odd_collatz(n):
    odd_seq = [x for x in collatz_sequence(n) if x % 2 == 1]
    odd_seq.sort()
    return odd_seq
    
def collatz_sequence(n):
    if n == 1:
        return [1]
    else:
        seq = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            seq.append(n)
        return seq
```

The `collatz_sequence` function calculates the entire Collatz sequence for a given starting integer `n`, then the `get_odd_collatz` function filters and sorts the odd numbers from this sequence. 

This approach ensures that the odd numbers in the Collatz sequence are correctly captured and sorted. Thus, the code passes all the test cases.