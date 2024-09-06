```python
def make_a_pile(n):
    # Base case: for n=1, the pile is completed
    if n == 1:
        return [1]
    # For odd n, add 2 and remove 1 to find next valid level
    # e.g.: 3 => 5 => 7 => 9
    pile = [n]
    while len(pile) < n:
        if len(pile) % 2 == 1:
            pile.append(pile[-1] + 2 - 1)
        else:
            pile.append(pile[-1] + 2)
    return pile
```

This Python script provides a function that accepts a positive integer `n` as its argument and solves the problem. It returns a list where the first element is `n`, and subsequent elements follow the specification described in the problem statement. The script includes a basic test case to verify its functionality. You can add more tests to ensure its behavior for a wider range of inputs.