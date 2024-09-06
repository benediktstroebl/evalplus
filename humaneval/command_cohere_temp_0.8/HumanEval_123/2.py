```python
def get_odd_collatz(n):
    odd_seq = [x for x in collatz_sequence(n) if x % 2 != 0]
    return sorted(odd_seq)

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

The `get_odd_collatz` function retrieves the odd numbers from the Collatz sequence for a given starting integer `n`. The `collatz_sequence` function calculates the entire Collatz sequence for `n`, both odd and even numbers, and the former is extracted by filtering from this sequence. The resulting odd numbers are then sorted in ascending order. 

This approach ensures that the odd numbers in the Collatz sequence are accurately extracted and returned, matching the specification of the problem. Test cases can easily be performed to validate the function with various starting values.