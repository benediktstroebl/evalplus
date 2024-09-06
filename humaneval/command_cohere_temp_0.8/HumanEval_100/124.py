```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if len(pile) % 2 == 0 and pile[-1] % 2 == 0:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```

This script defines a function `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. The function initializes a list `pile` with the first level of stones, iteratively adding stones to the next level based on whether the previous level's number of stones was odd or even. It then returns the list of stone counts for each level.

The script self-containtsly as it doesn't rely on any external variables or modules, and it can be executed independently. I hope this helps solve your problem! Let me know if you have any other questions.