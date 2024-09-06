```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```
This Python script provides a function that takes in two lists, `game` and `guess`, and returns a list of corrections, where each element corresponds to the difference between the two lists for the corresponding game and guess. The function uses a list comprehension, which includes a check to determine if the elements of `game` and `guess` at each index are equal. If they are, the result is 0, and otherwise, the result is the absolute difference between the two elements.