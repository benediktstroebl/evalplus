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
The function uses a simple iterative approach that follows the problem statement instructions to build the pile. It maintains a list `pile` that keeps growing level by level until it reaches the height of `n + 1` or more. At each step, it adds `1` to the next level if the current level is odd, and adds `2` if the current level is even, based on the logic of the problem. Finally, it returns the list `pile`.