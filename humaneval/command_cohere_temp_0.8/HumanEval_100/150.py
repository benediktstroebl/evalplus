```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n+1:
        if len(pile) % 2 == 1:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```
This script defines a function 'make_a_pile' that takes a single argument 'n', representing the number of stones in the first level of the pile. It constructs a list 'pile' with 'n' elements, where each element represents the number of stones in each level of the pile. The algorithm iteratively calculates the number of stones for the next level by adding 1 to the previous level's count if 'n' is odd, and adding 2 to the previous level's count if 'n' is even. This process continues until the length of 'pile' reaches 'n' plus 1, indicating the completion of the pile. The final result is the list 'pile', where each element represents the number of stones in each level of the pile.