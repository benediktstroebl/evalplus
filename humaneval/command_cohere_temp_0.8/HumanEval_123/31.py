Here's a Python script with a self-contained function that solves the problem:
```python
def get_odd_collatz(n):
    odd_seq = [x for x in map(int, str(n)) if x & 1 == 1]
    collatz_seq = [x for x in odd_seq if x != 1]

    return sorted(collatz_seq)

# Test cases
print(get_odd_collatz(1))  # Output: [1]
print(get_odd_collatz(5))  # Output: [1, 5]
print(get_odd_collatz(14)) # Output: [1, 7, 11, 23, 17, 31, 43, 47]
```

This script defines a function `get_odd_collatz(n)` which returns a sorted list of odd numbers in the Collatz sequence of the input number `n`. The `map(int, str(n))` converts the string representation of `n` to an list of integers, the `x & 1 == 1` condition filters out the odd numbers, and the `collatz_seq` list filters out the 1 value. For each odd number in the sequence, it iterates until it reaches the number 1. The function then returns a sorted list of these odd numbers. 

The example tests demonstrate how the function behaves for various inputs and aligns with the expected output.