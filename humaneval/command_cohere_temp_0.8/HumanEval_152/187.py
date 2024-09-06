```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game,guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the actual outcome of a match and the predicted outcome, respectively. It returns an array of the same length, where each element represents the absolute difference between the predicted and actual outcomes if they are different, and 0 if the guess was correct.