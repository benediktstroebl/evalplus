```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n+1:
        if len(pile) % 2 == 0:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```
This Python script defines a function named `make_a_pile` that addresses the problem statement. The function takes a single argument, `n`, representing the number of stones in the first level of the pile. It initially creates a starting pile with one element (n). Then, it enters a loop that continues until the pile contains `n+1` elements. Within each iteration, the loop considers whether the current length of the pile is even or odd to determine whether the next level should have the next odd or even number of stones. The size of the pile is consistently increased by 2 if the length is even, and by 1 if the length is odd, creating a pattern where each level has one more stone than the previous level. Finally, the function returns the completed pile as a list, representing the number of stones in each level.