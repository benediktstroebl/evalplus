```python
def make_a_pile(n):
    if n == 0:
        return []
    pile = [n]
    while len(pile) < n + 1:
        if len(pile) % 2 == 1 and pile[-1] % 2 == 0:
            pile.append(pile[-1] + 1)
        elif len(pile) % 2 == 0 and pile[-1] % 2 == 1:
            pile.append(pile[-1] - 1)
        else:
            pile.append(pile[-1])
    return pile
```

The code uses a simple `while` loop that iteratively adds to the pile (`pile`) based on the given rules. It checks whether the current `pile` length is odd and the previous stone was even, then it adds 1 to the previous stone. Otherwise, it checks whether the current `pile` length is even and the previous stone was odd, then it subtracts 1 from the previous stone. If neither of these conditions is met, it simply adds the previous stone to the `pile`. The loop stops when the length of the `pile` reaches `n + 1`.