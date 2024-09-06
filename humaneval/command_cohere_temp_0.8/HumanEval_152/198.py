```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```

The Python script provides a function, `compare`, which takes in two arrays, `game` and `guess`, where each element corresponds to the score of a match and a person's guess regarding the result of the same match. The function returns a list where each element denotes how far off each guess was regarding the actual score of the match. If the person's guess corresponds to the actual score for a match, the value in the returned list is 0. The function utilizes list comprehension and the `abs` function to compute the absolute difference between guesses and scores, respectively, and returns the resulting list of errors.