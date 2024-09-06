```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game,guess)]
```
This function takes two equal-length lists, `game` and `guess`, as arguments. It returns a list where each element is the absolute difference between the two lists if the guess is wrong, or 0 if the guess is correct. The list is returned after each element of the two lists is paired using the `zip` function, and the absolute difference is calculated using the `abs` function.