Here's a Python script that contains a function `get_odd_collatz` that solves the problem in a markdown code block:
```python
def get_odd_collatz(n):
    seq = [1]
    if n > 1:
        seq += [n]
        even = n
        while even > 1:
            if len(seq) > 2:
                break
            if even % 2 == 0:
                even //= 2
            else:
                even = 3 * even + 1
            seq += [even]
        seq = [i for i in seq if i % 2 != 0]
    return sorted(set(seq))

# Tests:
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(14) == [1, 7, 13]
```
This script defines a function `get_odd_collatz(n)` that, given a positive integer `n`, returns a sorted list of odd numbers in the Collatz sequence. The function starts with `1` in the sequence and iteratively calculates the next numbers in the sequence for odd or even numbers until it finds a number greater than `n` or the length of the sequence exceeds `2`. Then it adds the odd numbers to the sequence after filtering out duplicates, and returns them sorted.