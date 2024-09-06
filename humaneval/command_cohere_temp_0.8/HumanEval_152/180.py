```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It compares the elements of these arrays, pairing each element of `game` with its corresponding element in `guess`. It calculates the absolute difference between each pair of elements, resulting in an array of differences. However, if a pair of elements is equal, it sets the corresponding difference to 0, indicating a correct guess. Finally, it returns this array of differences.