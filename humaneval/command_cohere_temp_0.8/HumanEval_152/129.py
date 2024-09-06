```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The function uses Python's `zip` to iterate over the elements of the `game` and `guess` arrays pass each pair of elements to a `list` comprehension which checks if the elements in each pair are equal, using the `!=` operator (`x!=y`). If they are not equal, it calculates the absolute difference between the two elements using the `abs` function and assigns this value to the resulting list (`result`) at the corresponding index. If the elements are equal, it assigns `0` to the `result` at the corresponding index. Finally, the function returns the `result` list.