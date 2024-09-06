```python
def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]

    # Loop through and calculate the number of stones for each level based on the given rules
    for i in range(1, n.bit_length() + 1):
        if n & (1 << i) != 0:  # If the current bit is set to 1, it's odd, so multiply by 3
            pile.append(pile[-1] * 3)
        else:  # else it's even, so multiply by 2
            pile.append(pile[-1] * 2)

    return pile

# Example usage
print(make_a_pile(3))  # Should print: [3, 5, 7]
```

This script defines a function `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level, and returns a list containing the number of stones in each level. It iterates from the least significant bit to the most significant bit of `n`'s binary representation, and for each set bit, it multiplies the previous level's number of stones by 3 to produce the next level's number of stones if the current bit is 1, and by 2 if the current bit is 0. The resulting list reflects the desired arrangement of stone counts in each level of the pile.