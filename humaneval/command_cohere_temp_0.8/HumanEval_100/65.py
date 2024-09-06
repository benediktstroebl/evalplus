```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n+1:
        if len(pile) % 2 == 1:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```
This Python script defines a function called `make_a_pile` that takes a single argument `n`, representing the number of stones needed for each level in the pile. The function first creates a list called `pile` with `n` stones on the first level. It then enters a while loop that continues until the length of the `pile` reaches `n+1`. Within each iteration, the loop adds a new stone to the pile based on the following rules:
If the length of the pile is odd (including the first iteration where `n` is odd), it adds 2 stones to the pile. If the length of the pile is even, it adds 1 stone to the pile. This process continues until the pile has `n+1` levels.

Finally, the function returns the `pile` list, which contains the number of stones for each level of the pile.