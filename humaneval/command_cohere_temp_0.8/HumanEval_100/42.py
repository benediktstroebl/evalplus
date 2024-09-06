```python
def make_a_pile(n):
    # Base case: if n is 0, return a list with a single 0
    if n == 0:
        return [0]
    # For the base case of odd levels, and the recursive case, we calculate the
    # next odd integer using num_stones odd property
    num_stones = n
    # For even levels we calculate the next even integer using int(n/2) to
    # represent the integer division of n by 2, which yields the next even number
    if n % 2 == 0:
        num_stones = int(n / 2)
    # Initialize the pile with the current number of stones,
    # then recursively calculate the rest of the pile
    pile = [num_stones]
    return pile + make_a_pile(num_stones)
```

This approach takes advantage of the fact that the problem is inherently recursive, where each level's stone count depends on the previous one. The solution is to identify the pattern in the problem statement and express it in recursive terms.