```python
def make_a_pile(n):
    # Initialize a list to store the number of stones per level
    pile = [n]
    
    # Loop to create subsequent levels
    for i in range(1, n // 2 + 1):
        if i % 2 == 1:
            pile.append(i * 3 - 1)
        else:
            pile.append(i * 2)
    
    return pile
```

This Python script defines a function, `make_a_pile(n)`, that takes a positive integer `n` as input, simulates the process of building a pile of stones described in the problem, and returns a list representing the number of stones in each level.

Here's a breakdown of the code:
1.  The function starts by initializing an empty list called `pile` to store the number of stones per level.
2.  It then enters a loop that iterates from the second level (index 1) up to the halfway point of `n` (i.e., `n // 2 + 1`). This loop handles the creation of subsequent levels of the stone pile.
3.  Within the loop, it checks if the current level's number of stones should be odd or even based on the parity of the loop index `i`. 
    -   If `i` is odd, it calculates the next odd number by subtracting 1 from `i` and multiplying by 3. This ensures the pile grows by 3 stones on each odd level.
    -   If `i` is even, it simply multiplies `i` by 2 to grow the pile by 2 stones on each even level.
4.  Regardless of the parity, the calculated number of stones for the current level is appended to the `pile` list.
5.  Finally, the function returns the `pile` list, which represents the number of stones in each level of the pile.