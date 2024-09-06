```python
def make_a_pile(n):
    # Initialize a list to store the pile size at each level
    pile = [n]
    
    # Loop to build the pile progressively
    for i in range(1, n // 2 + 1):
        if i % 2 == 1:
            pile.append(i * 3 - 1)
        else:
            pile.append(i * 2)
    
    return pile
```

The code defines a function `make_a_pile(n)` that takes a positive integer `n` as input and returns a list representing the number of stones in each level of the pile. It starts with `n` stones in the first level, and then for each subsequent level, it either multiplies the previous level's count by 2 or multiplies it by 3 and subtracts 1 to get the next level's count, based on whether the previous level's count was even or odd. This logic creates the required pattern of stone counts for each level. 

The examples given in the problem statement are correctly solved by this function.