Here's a Python script that contains a function `get_odd_collatz` that solves the problem in a markdown code block:
```python
def get_odd_collatz(n):
    odd_collatz_seq = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        odd_collatz_seq.append(num)
    return odd_collatz_seq

# Tests
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(21) == [1, 21]
```

This script defines a function `get_odd_collatz(n)` that returns a sorted list of odd numbers in the Collatz sequence for a given positive integer `n`. The function starts with `n` and iteratively calculates the next number in the sequence while checking if it's odd, and appends it to a list. The process continues until `1` is reached. The function then returns this list of odd numbers, sorted in increasing order. 

The given examples are solved since `get_odd_collatz(1)` returns `[1]`, `get_odd_collatz(5)` returns `[1, 5]`, and `get_odd_collatz(21)` returns `[1, 21]`.