```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It iterates through the elements of these arrays using the `zip` function, comparing each element pairs. If the elements match, it assigns 0 to the corresponding index of the `result` array. Otherwise, it calculates the absolute difference between the elements and assigns that value to the corresponding index of the `result` array. Finally, it returns the `result` array, containing the differences or 0 for correct guesses.