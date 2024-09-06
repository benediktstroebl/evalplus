```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns a list where each element represents the difference between the corresponding elements in the `game` and `guess` arrays, or 0 if the guess was correct. This is done using the `zip` function to iterate through corresponding elements of both arrays and calculating the absolute difference, if they don't match, and the result is then returned in a list. Overall, the function computes the perceived error in each guess in the `guess` array relative to the actual game scores in the `game` array, resulting in an array of errors, with 0s at spots where the guess was correct.