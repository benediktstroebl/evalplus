```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns an array of the same length as the input arrays, where each element represents the difference between the corresponding elements in the `game` and `guess` arrays. If the guess is correct, the value is 0, otherwise, it is the absolute difference between the guess and the score. This accurately reflects the scenario of someone guessing the outcomes of matches, with the function providing feedback on how far off each guess was.