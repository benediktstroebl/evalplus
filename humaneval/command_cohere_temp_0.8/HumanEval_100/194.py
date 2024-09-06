```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n+1:
        if len(pile) % 2 == 0 and pile[-1] % 2 == 0:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```
This code defines a function `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. It uses a list `pile` to keep track of the number of stones in each level. Initially, `pile` contains only the number of stones for the first level.

The while loop runs until the length of the `pile` reaches `n+1`, indicating that all `n+1` levels of the pile have been constructed. Within the loop, it adjusts the next level's stone count based on whether the previous level's count was odd or even. If the previous level's count is even and its last digit is even, it adds 2 to the count; otherwise, it adds 1 to the count.

Finally, it returns the `pile`, which now contains the number of stones for each level of the pile, including the first level.