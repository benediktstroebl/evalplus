```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The Python script provides a function called `compare` which takes two arrays, `game` and `guess`, where each element denotes a match. The function calculates the absolute difference between each pair of corresponding elements in `game` and `guess` and stores the results in a list called `result`. If the elements match, the function assigns a value of 0 to this list. Finally, it returns the `result` list, which contains how far off each guess was.