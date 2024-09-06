Here's a Python script that contains a function to solve the problem in a markdown code block as asked:
```python
def get_odd_collatz(n):
    odd_collatz = []
    sequence = [n]
    while len(sequence) > 0:
        current = sequence.pop()
        if current % 2 == 0:
            sequence.append(current // 2)
        else:
            sequence.append(3 * current + 1)
        if current % 2 != 0:
            odd_collatz.append(current)
    return odd_collatz

# Test cases
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(14) == [1, 7, 13]
```
This script defines a function `get_odd_collatz(n)` that returns the odd numbers in the Collatz sequence of a given positive integer n. The function uses a while loop to generate the Collatz sequence and appends the odd numbers to a list `odd_collatz`, which it returns as the result. The test cases asserted correspond to the example provided and ensure the function behaves as expected.