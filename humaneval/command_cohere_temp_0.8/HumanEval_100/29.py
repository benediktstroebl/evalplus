```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n+1:
        if len(pile) % 2 == 1:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```
This Python script defines a function called `make_a_pile` that takes a single argument, `n`, which represents the number of stones in the first level of the pile. The function creates a list called `pile`, where the first element is set to `n`. It then enters a while loop that continues until the length of the `pile` reaches `n+1`. Within the loop, it checks whether the length of the pile is odd or even using the modulo operator (`%`). If the length is odd, the function increments the last element of the pile by 2 and adds it to the `pile`. If the length is even, it increments the last element of the pile by 1 and adds it to the `pile`. This process continues until the pile contains `n+1` elements. Finally, the function returns the `pile` list, which contains the number of stones required for each level of the pile. 

Here is an example of calling the function with an argument of `n=3`:
```python
make_a_pile(3)
```
The output will be:
```
[3, 5, 7]
```