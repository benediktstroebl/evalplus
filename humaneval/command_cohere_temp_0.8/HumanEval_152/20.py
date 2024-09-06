```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It compares the elements of these arrays, which represent game scores and user guesses respectively, pairwise using `zip`, and calculates the absolute difference between them, storing the results in a list. However, if a guess is correct (i.e., the elements are equal), it sets the corresponding result to 0. The final result list is then returned, representing how far off each guess was from the actual scores.