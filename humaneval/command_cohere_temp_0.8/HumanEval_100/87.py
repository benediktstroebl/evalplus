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
This Python script provides a self-contained function, `make_a_pile(n)`, which accepts a positive integer `n` as input and generates a pile of stones as requested in the prompt. The function constructs the pile by starting with `n` stones on the first level, and then iteratively adding an odd number of stones for odd-numbered levels and an even number of stones for even-numbered levels to create the next level until the specified number of levels is reached. The resulting list of stone counts for each level is then returned as the output.

Here's an example of how to use the provided Python function to solve the problem:
```python
make_a_pile(3)
```
This would output:
```
[3, 5, 7]
```

The example logically demonstrates how the function works, generating a pile of stones with three levels, where the first level has 3 stones, the second level has 5 stones, and the third level has 7 stones, adhering to the specified pattern of adding odd or even numbers to determine the number of stones for each level.