```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n+1:
        if n % 2 == 1:
            n += 2
        else:
            n += 1
        pile.append(n)
    return pile
```
This function uses a simple iterative approach to create the pile, ensuring that the number of stones at each level follows the problem statement's rules. The loop increments the value of `n` and adds it to the pile if it's currently odd or if it's even, respectively. The process continues until the pile has `n+1` number of elements, ensuring it has the correct number of levels as specified in the problem. The resulting pile of stones is returned as a list, where the index of the list corresponds to the level of the pile.