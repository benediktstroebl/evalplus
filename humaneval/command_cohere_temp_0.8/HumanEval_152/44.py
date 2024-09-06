```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The function compares the elements of the `game` and `guess` arrays on a one-to-one basis utilizing the `zip` function. It calculates the absolute difference between the values for each corresponding element and assigns the result to the `result` variable. If the elements match, it assigns `0` to the `result` instead. Finally, the function returns the `result` array, which contains the how far off each guess was for each corresponding pair of elements.