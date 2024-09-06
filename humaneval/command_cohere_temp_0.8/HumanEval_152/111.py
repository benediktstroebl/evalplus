```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```

The function uses a list comprehension that loops through pairs of corresponding elements in `game` and `guess` arrays. If the elements don't match, the resulting value is the absolute difference between them. If the elements match, the resulting value is 0. Ultimately, the resulting list is returned, containing the sequence of values representing the difference (or 0) for each pair.