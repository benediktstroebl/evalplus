```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```

The function compares each element of `game` and `guess` arrays and returns an array of the same size, `result`, where each element denotes how far off each guess was from the corresponding game result. The function returns 0 if the guess was correct.