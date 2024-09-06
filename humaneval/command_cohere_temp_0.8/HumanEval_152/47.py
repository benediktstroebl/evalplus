```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It compares the elements of the two arrays element-wise, calculating the absolute difference between each element if they don't match, and 0 if the guess was correct. The resulting array of differences is then returned.