```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It compares the elements of these arrays, pairing each element of `game` with the corresponding element of `guess` using the zip function. For each pair of elements, it calculates the absolute difference between them if they are not equal, indicating a wrong guess. Otherwise, it assigns a value of 0 to indicate a correct guess. Finally, the function returns a new array containing these calculated values, representing how far off each guess was from the actual game results.