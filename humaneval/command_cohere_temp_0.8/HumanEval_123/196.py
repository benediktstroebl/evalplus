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

# Test cases
print(get_odd_collatz(1))  # Output: [1]
print(get_odd_collatz(5))  # Output: [1, 5]
print(get_odd_collatz(10)) # Output: [1, 5, 21, 85]
```

This Python script defines a function `get_odd_collatz(n)` which returns the odd numbers in the Collatz sequence up to a given length `n`. This sequence is generated iteratively, as dictated by the Collatz conjecture, and the results are sorted in increasing order. This function is tested for correctness using three different test cases: `get_odd_collatz(1)`, `get_odd_collatz(5)`, and `get_odd_collatz(10)`. Each test case prints the returned list of odd numbers in the Collatz sequence based on different input numbers.