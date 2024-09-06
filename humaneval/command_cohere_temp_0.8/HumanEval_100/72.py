```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if n % 2 == 1:
            n += 2
            pile.append(n)
        else:
            n += 1
            pile.append(n)
    return pile
```

The function uses a simple loop that iterates through numbers incrementing by 2 or 1, accordingly, to create the required `pile` of stones. The loop continues until the next level of the pile (number of stones) is less than or equal to the current level, guaranteeing that the pile contains `n` levels with the correct number of stones.