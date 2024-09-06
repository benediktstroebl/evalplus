```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if len(pile) % 2 == 0 and pile[-1] % 2 == 0:
            pile.append(pile[-1] + 2)
        elif len(pile) % 2 == 1 or pile[-1] % 2 == 1:
            pile.append(pile[-1] + 1)
        else:
            raise Exception('Something went wrong')
    return pile
```

This Python script defines a function named `make_a_pile` that addresses the problem statement. The function takes an integer `n` as input and constructs a pile of stones where each level contains stones based on the rule outlined in the problem statement. It starts with `n` stones in the first level and then calculates the number of stones for the next level according to the specified rules.

The script uses a `while` loop to generate the pile level by level until the total number of levels reaches `n + 1`. It pays attention to whether the current level's number of stones is odd or even and then determines the next level's count accordingly. The resulting list of stone counts for each level is then returned.

The example usage provided in the problem statement shows how to use this function, and the output is also provided as a comment in the code snippet.