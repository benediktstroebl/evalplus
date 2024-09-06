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
The function starts with a base case of `n` stones in the first level. It then iteratively adds either the next even number or the next odd number to the pile depending on whether `n` is even or odd, respectively. This is done until the pile contains `n + 1` stones, ensuring there are `n` levels of stones in the pile.