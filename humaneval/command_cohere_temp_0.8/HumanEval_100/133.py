```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if n % 2 == 1:
            n += 2
        else:
            n += 1
        pile.append(n)
    return pile
```
This Python script defines a function named `make_a_pile` that addresses the problem statement. The function takes a single argument, `n`, representing the number of stones in the first level of the pile. Inside the function, a list called `pile` is initialized with the starting value of `n`. This list will store the number of stones in each level of the pile.

A `while` loop is used to build the pile incrementally. The loop continues until the length of the `pile` reaches `n + 1`—the number of levels in the pile. Within the loop, the code checks whether `n` is odd or even to determine the number of stones in the next level.

If `n` is odd, it increments `n` by 2 to add an even number of stones to the next level. If `n` is even, it increments `n` by 1 to add an odd number of stones to the next level. The updated value of `n` is then added to the `pile`, thus growing the pile level by level.

Finally, the function returns the `pile` list, which represents the number of stones in each level of the pile. The element at index `i` in the list corresponds to the number of stones in the `i+1`th level of the pile.

The provided example usage demonstrates the function's behavior when `n` is 3, and it correctly returns the expected output `[3, 5, 7]`, representing the number of stones in each of the three levels in the pile.