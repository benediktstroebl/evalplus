```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if len(pile) % 2 == 1:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```
This Python script defines a function called `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. The function initiates a list called `pile` with the first level's stone count (`n`). It then enters a while loop that continues until the length of the `pile` reaches `n + 1`. Within the loop, it checks whether the length of the `pile` is odd using the modulo operator (`%`). If it's odd, the next level's stone count is calculated by adding 2 to the previous level's count. If it's even, it adds 1 to the previous level's count. This process repeats until the `pile` reaches the desired length. Finally, the function returns the `pile` list, containing the counts of stones for each level of the pile.