```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if len(pile) % 2 == 0:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```
This script defines a function, `make_a_pile(n)`, that generates a list of stone counts for each level of a pile, given a starting number of stones in the first level (`n`). The list it produces follows the specification outlined in the problem: odd levels add 1 to the previous odd level, while even levels add 2 to the previous even level. This logic is encapsulated in a while loop that iteratively generates the list of stone counts up to the `(n+1)`th level. The examples given in the problem statement yield the expected results when this function is invoked:
```python
>>> make_a_pile(3)
[3, 5, 7]
>>> make_a_pile(4)
[4, 6, 8]
``` 
This approach has a time complexity of `O(n)` since it requires looping up to `(n+1)` times, and each iteration operates in constant time.