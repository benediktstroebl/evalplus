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
This Python script defines a function named `make_a_pile` that addresses the problem statement. It takes a single argument `n`, representing the number of stones in the first level of the pile. The function creates a list called `pile`, where each element represents the number of stones in each level. It starts with `n` stones in the first level, and then, using a `while` loop, it predicts the number of stones for the next level based on whether the current level is odd or even. It then appends this predicted number to the `pile` and continues this process until the total number of levels reaches `n + 1`. The final list `pile` contains the number of stones for each level, and it's returned as the function's output.