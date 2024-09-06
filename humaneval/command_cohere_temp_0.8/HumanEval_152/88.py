```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It compares the elements of these arrays, which represent game scores and user guesses respectively, pairwise using `zip`, and calculates the absolute difference between them if they don't match, resulting in a list of errors. If a guess matches the corresponding score, the error is set to 0. The resulting list of errors is returned as the output of the function.