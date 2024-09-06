```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It compares the elements of these arrays, which represent game scores and user guesses respectively, iterating through each pair of elements using the `zip` function. It calculates the absolute difference between each pair, determining whether the user's guess was correct by checking if the absolute difference is zero. If the guess is correct, it sets the result to 0. The resulting list of differences or 0s is then returned as the output.