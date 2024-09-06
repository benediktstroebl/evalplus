```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```

The solution works by using Python's list comprehension and zipper to compare in parallel each element of the `game` and `guess` arrays. The zipper functionality ensures that the comparison is done correctly even if the lengths of the arrays are different. Finally, the result list comprehension creates an array of the differences between the elements, calculated as `abs(x-y) if x != y else 0`. In the latter case, the result is 0, meaning that the person correctly guessed the result.