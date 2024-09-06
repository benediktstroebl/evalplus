Here's a Python script that contains a function `get_odd_collatz` that solves the problem in a markdown code block:
```python
def get_odd_collatz(n):
    seq = [1]
    if n > 1:
        seq += [n]
        even = n
        while even > 1:
            if len(seq) > 1000:
                break
            if even % 2 == 0:
                even //= 2
            else:
                even = 3 * even + 1
            if even % 2 != 0:
                seq += [even]
    return sorted(set(seq) - {1})
```

This script defines a function `get_odd_collatz(n)` that takes a positive integer `n` as input and returns a sorted list of odd numbers in the Collatz sequence. The function includes a check to limit the sequence length to avoid infinite loops. It then uses a set to remove duplicate entries, specifically removing the single odd number in the sequence, as Collatz(1) is [1]. The output is finally sorted to provide an increasing list.