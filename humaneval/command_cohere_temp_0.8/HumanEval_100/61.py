```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if n % 2 == 0:
            n += 2
        else:
            n += 1
        pile.append(n)
    return pile
```
This Python script defines a function named `make_a_pile` that takes a single argument `n`, representing the number of stones needed at the first level of the pile. The function returns a list where each element represents the number of stones needed at the corresponding level of the pile. It starts with `n` stones at level 1 and increments the count at each even or odd level based on the initial value of `n`. The condition `len(pile) < n + 1` ensures that the loop only runs until the desired number of levels is reached.