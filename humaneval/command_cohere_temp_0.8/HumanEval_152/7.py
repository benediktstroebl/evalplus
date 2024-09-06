```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game,guess)]
```
This function takes two equal-length lists, `game` and `guess`, where each element corresponds to the actual outcome of a match and the predicted outcome, respectively. It returns a list where each element is either 0, if the prediction was correct, or the absolute difference between the prediction and the actual outcome if not.