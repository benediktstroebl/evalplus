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
This Python script defines a function called `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. The function proceeds to create a list (`pile`) where each element represents the number of stones in a respective level of the pile. It starts with `n` stones in the first level, and then, iteratively, it calculates the number of stones for the next level. If the current level has an odd number of stones (`len(pile)` is odd), it adds 2 to the current number of stones to determine the count for the next level. If the current level has an even number of stones, it increments the current count by 1 to determine the number of stones for the next level. This process continues until `pile` contains `n + 1` elements, meeting the requirement for the pile's length. The resulting `pile` list is then returned, representing the number of stones in each level of the pile.