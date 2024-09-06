```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns a list where each element represents the difference between the corresponding elements in the `game` and `guess` arrays, or 0 if the guess was correct. The function iterates through the elements of the two arrays using the `zip` function, calculating the absolute difference between the scores and guesses for each match. If the guess was correct, it returns 0. The result is a list that shows how far off each guess was.