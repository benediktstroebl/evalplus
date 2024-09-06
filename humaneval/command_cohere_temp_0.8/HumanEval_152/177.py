```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length lists, `game` and `guess`, where each element corresponds to the score of a match, and returns an array of the same length containing zero if the guess was correct, and the absolute difference between the guess and the score otherwise. This is done using the `zip` function to iterate through the elements of both lists simultaneously.