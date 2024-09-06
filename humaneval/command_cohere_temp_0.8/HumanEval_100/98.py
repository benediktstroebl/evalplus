```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n+1:
        if len(pile) % 2 == 0:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```
This Python script defines a function called `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. The function initiates a list called `pile` with the first level's stone count (`n`). It then enters a while loop that continues until the length of the `pile` reaches `n+1`. Within the loop, it checks whether the length of the `pile` is even or odd to determine the number of stones needed for the next level. If the length is even, it adds 2 to the last element of the `pile`; if the length is odd, it adds 1 to the last element. This process effectively builds the required pile of stones. Finally, the function returns the `pile` list, which now contains the number of stones required for each level of the pile.