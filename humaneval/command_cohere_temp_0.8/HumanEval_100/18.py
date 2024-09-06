```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n+1:
        if n % 2 == 1:
            n += 2
        else:
            n += 1
        pile.append(n)
    return pile
```
This script defines a function `make_a_pile` that takes a positive integer `n` as input and returns a list of stone counts for each level of the pile. It starts with `n` stones on the first level, and for each subsequent level, it increments `n` by 2 if the previous `n` was odd, and by 1 if the previous `n` was even. This way, the pile grows in a staggered manner, with each level having one more stone than the previous level.