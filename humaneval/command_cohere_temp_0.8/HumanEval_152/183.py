```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It compares the elements of these arrays, which represent game scores and user guesses respectively, pairwise using `zip`, and calculates the absolute difference between them if they are different, indicating that the user's guess was incorrect. If the elements are equal, it assigns a value of 0 to indicate a correct guess. It then creates a list `result` based on these comparisons and returns this list as the output.