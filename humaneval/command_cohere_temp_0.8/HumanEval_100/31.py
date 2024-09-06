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
The function uses a simple iterative approach to create the pile, adding to the previous level in the list based on whether the length is odd or even. This approach is efficient and easy to understand, making it a suitable solution to the given problem. It also allows the function to handle any positive integer successfully.