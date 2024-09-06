```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if len(pile) % 2 == 0 and pile[-1] % 2 == 0:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```
The provided Python script defines a function called `make_a_pile` that takes a single argument `n`, representing the number of stones needed for each level in the pile. The function starts with a foundation of `n` stones for the first level and then iteratively constructs subsequent levels using a `while` loop. It ensures that each level has sequentially odd or even numbers of stones, building upon the previous number. The result is a list containing the count of stones for each level, including the initial `n` stones. This function effectively solves the problem statement and generates a list depicting the desired pile structure.