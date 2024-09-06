```python
def make_a_pile(n):
    # Get the next odd or even number based on the parity of n
    def get_next_parity_number(parity):
        return 2 * (parity - 1) + 1 if parity else 2

    # Generate the list of stone counts
    stone_counts = [n]
    for i in range(1, n.bit_length() + 1):
        stone_counts.append(get_next_parity_number(stone_counts[i] & 1))

    return stone_counts
```

This code defines a function `make_a_pile(n)` that takes a positive integer `n` as input and returns a list representing the number of stones in each level of the pile. It iteratively constructs the list, where each element at index `i` represents the number of stones in the level `(i+1)`. It follows the problem statement's guidelines, where the number of stones in the next level is determined by the next odd number if the previous level's count (`stone_counts[i]`) is odd, and the next even number if it's even. This logic is encapsulated in the helper function `get_next_parity_number`, optimizing the parity calculation. The result is a list of stone counts that forms the desired pile structure.