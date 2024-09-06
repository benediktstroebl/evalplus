```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The solution works by using Python's `zip()` function to iterate over the elements of the `game` and `guess` arrays simultaneously, calculating the difference between each element and storing the result in a new list. If the elements are equal, the result is `0`, otherwise, the absolute difference is calculated and stored in the resulting list. The resulting list reflects how far off each guess was.