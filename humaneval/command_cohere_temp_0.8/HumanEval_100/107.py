```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if len(pile) % 2 == 0:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```
This Python script defines a function called `make_a_pile` that takes a single argument, `n`, which represents the number of stones in the first level of the pile. The function creates a list called `pile`, where the first element is set to `n`. It then enters a while loop that continues until the length of the `pile` reaches `n + 1`. Within the loop, it checks whether the length of the pile is even or odd, and accordingly, it increments the previous element by 2 or 1. After each iteration, a new element is added to the pile. Finally, the function returns the `pile` list, which represents the number of stones in each level of the pile.