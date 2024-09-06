```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game,guess)]
```
This Python script defines a function named `compare` which takes two arrays, `game` and `guess`, as input. It returns an array of the same length as these inputs, where each element represents the difference between the corresponding elements of `game` and `guess`. If the guess matches the score, it returns `0`, otherwise it returns the absolute difference between the two values.