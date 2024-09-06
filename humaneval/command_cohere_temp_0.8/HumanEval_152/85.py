```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns a list where each element represents the similarity between the corresponding elements in the `game` and `guess` arrays. If the guess matches the correct outcome, it returns `0`, and if not, it calculates the absolute difference between the guess and the correct outcome.