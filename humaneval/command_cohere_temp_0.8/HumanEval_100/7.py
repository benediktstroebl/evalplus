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
The function uses a loop to create a list representing the stones in each level, starting with `n` stones on the first level. It enters the loop repeatedly until the pile size reaches `n+1`. Within the loop, it checks whether the pile size is odd or even using the modulo operator (`%`). If the size is odd, it increments the size by 2 for the next level, whereas if it's even, it increments the size by 1. The loop ensures that the pile grows incrementally according to the problem statement.