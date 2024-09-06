```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The function uses list comprehension and the `zip` function to iterate through each element of both arrays `game` and `guess` simultaneously. It compares the values at each index and calculates the absolute difference, assigning it to the result list. If the values at a certain index are the same, it assigns 0 to the `result` list, which indicates a correct guess. 

The resulting list `result` is of the same length as the given arrays, where each index holds the correspondence between the guesses and the actual results, denoting how far off the guesses were.