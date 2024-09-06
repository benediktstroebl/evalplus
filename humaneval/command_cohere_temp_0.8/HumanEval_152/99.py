```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It iterates through the elements of `game` and `guess` simultaneously using the `zip` function, calculating the absolute difference between each element if they don't match, or assigning 0 if the guess was correct. The resulting list of differences or 0s is then returned as the output of the function.