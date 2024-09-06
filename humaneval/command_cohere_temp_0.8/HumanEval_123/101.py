Here's a Python script that contains a function `get_odd_collatz` that solves the problem in a markdown code block:
```python
def get_odd_collatz(n):
    seq = [1]
    while len(seq) < len(str(n)):
        if seq[-1] % 2 == 0:
            seq.append(seq[-1] // 2)
        else:
            seq.append(3 * seq[-1] + 1)
    return [e for e in seq if e % 2 != 0]

# Test cases
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(14) == [1, 7, 13]
```

This script defines a function `get_odd_collatz(n)` that returns the odd numbers in the Collatz sequence of a given positive integer `n`. The function starts with `1` in the sequence and iteratively calculates the next numbers in the sequence (either by halving or tripling and adding 1, as per the Collatz conjecture rules). Finally, it returns a list of odd numbers in the sequence up to and including `n`. The test cases assert that the function produces the expected results for `n` values of `1`, `5`, and `14`.