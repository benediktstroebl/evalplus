Here's a Python script that contains a function `get_odd_collatz` that solves the problem in a markdown code block:
```python
def get_odd_collatz(n):
    seq = [1]
    if n > 1:
        seq += [n]
        odd_seq = [x for x in seq if x % 2 != 0]
    return odd_seq

# Tests:
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(14) == [1, 7, 13]
```
This script defines a function `get_odd_collatz(n)` that returns a list of odd numbers in the Collatz sequence of the given positive integer `n`. The script then includes some tests that can be used to verify the functionality of the code. You can add more tests to further validate the function for other input cases.