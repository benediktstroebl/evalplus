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
This code defines a function make_a_pile() that takes a positive integer n as input and creates a pile of n levels of stones. It starts with the first level having n stones, and then for each subsequent level, it either adds 1 or 2 stones compared to the previous level depending on whether the previous level's size was odd or even, respectively. The function returns a list containing the number of stones for each level.