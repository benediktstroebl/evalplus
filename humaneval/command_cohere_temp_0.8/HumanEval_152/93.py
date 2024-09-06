```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
```
This Python script defines a function named `compare` which takes two arrays, `game` and `guess`, as input. It compares the elements of the two arrays pairwise using `zip`, checking if the guesses match the game results. If a guess matches the result, it returns 0, otherwise, it returns the absolute difference between the guess and the result. The results are then aggregated into a single array and returned.