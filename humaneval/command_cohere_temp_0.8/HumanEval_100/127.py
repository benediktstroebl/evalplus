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
This script defines a function `make_a_pile` that takes a positive integer `n` as input and returns a list representation of the pile, including the top layer (index 0) having `n` stones. It initializes the pile with a starting layer of `n` stones, and then iteratively adds layers using the condition `n % 2 == 1` for the next layer if the current layer is odd, and `n + 2` if the current layer is even, updating the `pile` accordingly. The condition for ending the loop is that the pile's length must be at least `n + 1`, ensuring the existence of all layers. Thus, the output list represents the stone count for each level of the pile, with index `i` representing the number of stones in the `i+1` level.