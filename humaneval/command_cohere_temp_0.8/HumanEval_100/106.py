```python
def make_a_pile(n):
    # Initialize a list to store the pile size at each level
    pile = [n]

    # Iterate through odd and even levels, updating pile size accordingly
    for i in range(1, n.bit_length() + 2):
        if i & 1:  # If level is odd, use next odd number
            pile.append(pile[-1] + 2)
        else:     # Otherwise, use next even number
            pile.append(pile[-1] + 1)

    return pile
```

This solution uses a simple loop to iterate through each level of the pile, determining whether the current level is odd or even, and incrementing the stone count accordingly. This ensures that the pile grows in the required fashion, and it returns the list of stone counts for each level.