```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The function compares the elements of the `game` and `guess` arrays on a one-to-one basis utilizing the `zip` function. It calculates the absolute difference between the values for each index if they don't match, and returns 0 if they do, yielding an array of results. The resulting array is then returned.