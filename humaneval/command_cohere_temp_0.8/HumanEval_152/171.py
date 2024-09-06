```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```

The function compares each element of `game` and `guess` and returns an array of the same size, filling it with the absolute difference between the two elements if they don't match, and 0 if they do. The code uses `zip` to iterate through `game` and `guess` simultaneously, and the `abs()` function is used to measure the difference between the values, as the problem statement instructs to return the absolute difference.