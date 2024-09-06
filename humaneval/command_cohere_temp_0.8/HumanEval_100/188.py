```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n+1:
        if len(pile) % 2 == 0 and pile[-1] % 2 == 0:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```
This Python script provides a self-contained function, `make_a_pile(n)`, which accepts a positive integer `n` as input and generates a pile of stones as specified in the problem statement. The function initializes the pile with `n` stones on the first level and then iteratively calculates the number of stones for the next level based on whether the previous level's number of stones was odd or even. It continues this process until the pile contains `n+1` elements, ensuring the pile has the correct number of stones on each level. The final result is a list containing the number of stones for each level, where the element at index `i` represents the number of stones in the level at index `i+1`.