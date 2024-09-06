```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```

The function compares each element of `game` and `guess` arrays and returns an array of the same size, where the value is the absolute difference between the guess and the score if the guess is wrong, and 0 if the guess is correct.