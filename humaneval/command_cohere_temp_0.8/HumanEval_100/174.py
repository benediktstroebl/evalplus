```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if n % 2 == 1:
            n += 2
        else:
            n += 1
        pile.append(n)
    return pile
```
This Python script defines a function called `make_a_pile` that takes a single argument `n`, representing the number of stones needed for each level in the pile. The function returns a list where each element represents the number of stones for each level. It starts with `n` stones in the first level, and for each subsequent level, it adds 2 if the previous number was odd, or 1 if the previous number was even, incrementing the count of stones in the pile.