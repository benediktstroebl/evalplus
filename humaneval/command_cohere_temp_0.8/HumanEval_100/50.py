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
This Python script defines a function called `make_a_pile` that takes a single argument, `n`, which represents the number of stones in the first level of the pile. The function creates a list called `pile`, where the first element is set to `n`. It then enters a loop that keeps running until the length of the `pile` is equal to `n+1`. 

Within the loop, it checks whether the length of the `pile` is even or odd, and accordingly, it calculates the next level's stone count:
- If the length is even, it appends the current length plus 2 to the `pile`.
- If the length is odd, it appends the current length plus 1 to the `pile`.

This way, the `pile` keeps growing until it has `n+1` elements, and the function returns this list `pile`.