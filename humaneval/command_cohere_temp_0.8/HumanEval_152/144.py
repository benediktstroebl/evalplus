```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The Python script provides a function called `compare` which takes two arrays, `game` and `guess`, where each element denotes a match. The function calculates the absolute difference between each pair of corresponding elements if they don't match, or returns 0 if the guess was correct. The result is then returned as an array of the same length as the input arrays, providing an array of how far off each guess was.