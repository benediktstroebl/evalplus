```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns a list where each element corresponds to the result of comparing the corresponding elements in the `game` and `guess` arrays. If the guess matches the game array element correctly, it returns 0, otherwise it returns the absolute difference between the two elements.