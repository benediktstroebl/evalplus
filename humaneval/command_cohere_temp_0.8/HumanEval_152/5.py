```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```

The function uses python's `zip` to iterate over elements of `game` and `guess` arrays systematically, storing the corresponding values in the `result` array with absolute differences if the values don't match or 0 if they do. 

This approach ensures that the returned array contains the appropriate values for each element of the input arrays, adhering to the problem's guidelines.