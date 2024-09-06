```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This Python script defines a function named `compare` which takes two arrays, `game` and `guess`, as input. It compares the elements of the two arrays pairwise using `zip`, checking if the guesses match the game results correctly. If a guess matches the result, it returns a list of 0s using a list comprehension, indicating an accurate prediction. If the guess doesn't match the result, it computes the absolute difference between the guess and the score for each pair, resulting in an array of discrepancies indicating how far off each guess was.