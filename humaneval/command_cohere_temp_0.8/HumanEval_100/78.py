```python
def make_a_pile(n):
    # Get the next odd or even number
    def get_next_number(current):
        return current + 2 if current % 2 else current + 1

    # Generate the pile of stones
    pile = [n]
    for i in range(1, n + 1):
        pile.append(get_next_number(pile[i - 1]))

    return pile
```

This code defines a function `make_a_pile(n)` that takes a positive integer `n` as input and returns a list of stone counts for each level of the pile, with element `i` representing the count for level `i + 1`. It generates the pile of stones following the given constraint.

The code works by:
1. Using a helper function, `get_next_number(current)`, to determine the next stone count based on the current level's count and its parity:
   - If the current count is odd, it computes the next odd number beyond it (`current + 2`).
   - If the current count is even, it computes the next even number beyond it (`current + 1`).
2. Starting with an initial count of `n` stones on the first level, it iterates through each subsequent level, updating the pile list with the calculated stone count for each level.