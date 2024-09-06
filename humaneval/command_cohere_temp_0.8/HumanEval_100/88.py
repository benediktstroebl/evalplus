```python
def make_a_pile(n):
    # Base case: for n=1, the pile is completed
    if n == 1:
        return [1]
    # For odd n, add 2 to the previous level and return it
    if n % 2 == 1:
        return [n] + [i + 2 for i in make_a_pile(n - 1)]
    # For even n, add 1 to the previous level and return it
    else:
        return [n] + [i + 1 for i in make_a_pile(n - 1)]
```

This approach uses a recursive strategy to construct the pile, ascertaining whether the current layer is odd or even to determine the subsequent layer's number of stones. The recursion is halted when the base case of n=1 is met, and a single stone constitutes a complete pile. Ultimately, the script produces a list of stone counts for each level.