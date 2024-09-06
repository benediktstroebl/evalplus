```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns a list where each element represents the difference between the corresponding elements in the `game` and `guess` arrays, or 0 if the guess was correct. This is done using the `zip` function to iterate through corresponding elements of both arrays and calculating the absolute difference, if they don't match, and the result is then returned as a list. Overall, this function computes the perceived error in someone's guesses about the results of games compared to the actual results in the `game` array.