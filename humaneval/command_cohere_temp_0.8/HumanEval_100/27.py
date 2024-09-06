```python
def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]
    
    # Loop to create the remaining levels
    for i in range(1, n // 2 + 1):
        if i % 2 == 1:
            pile.append(i * 3 - 1)
        else:
            pile.append(i * 2)
    
    return pile
```

This Python script defines a function called `make_a_pile` that takes a single argument, `n`, which represents the number of stones in the first level of the pile. Inside the function, the stack is initialized with the number `n`, and a loop iterates through the levels, alternating between odd and even numbers. The odd levels are calculated by multiplying the level number by 3 and subtracting 1, while the even levels are calculated by multiplying the level number by 2. The resulting number of stones in each level is stored in the `pile` list, which is then returned.