```python
def get_odd_collatz(n):
    odd_collatz = [1]
    while len(odd_collatz) < n:
        if len(odd_collatz) % 2 == 1:
            next_num = 3 * odd_collatz[-1] + 1
        else:
            next_num = odd_collatz[-1] // 2
        odd_collatz.append(next_num)
    return odd_collatz[:n]

# Test Cases
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(10) == [1, 5, 13]
```

This function uses an iterative approach to generate the odd numbers in the Collatz sequence up to a given `n`. It starts with `1` in the list, and progressively generates odd numbers based on the sequence rules, appending them to the list. The function returns the first `n` odd numbers in the sequence, as specified by the problem.