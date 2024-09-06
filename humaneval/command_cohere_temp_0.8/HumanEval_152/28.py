```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It iterates through the elements of these arrays using the `zip` function, comparing each element pair. If the elements don't match, it calculates the absolute difference between them and assigns the result to the `result` list. However, if the elements match, it assigns a value of 0 to the `result` list. Finally, it returns the `result` list, which represents how far off each guess was from the corresponding score in the `game` array.