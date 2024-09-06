```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns an array of the same length as the input arrays, where each element represents the difference between the corresponding elements in the `game` and `guess` arrays. If the guess was correct, the value is 0, otherwise, it is the absolute difference between the guess and the score. This function effectively compares each element in the `game` array with the corresponding element in the `guess` array and determines how far off each guess was, returning the results as an array.