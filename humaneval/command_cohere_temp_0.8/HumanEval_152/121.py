```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```
This Python script provides a function that takes two equal-length arrays, `game` and `guess`, where each element corresponds to the score of a matched game. The function returns an array of the same length, where each element denotes how far off each guess was from the corresponding score in the `game` array. If the guess was correct, the value is 0; otherwise, it is the absolute difference between the guess and the score.