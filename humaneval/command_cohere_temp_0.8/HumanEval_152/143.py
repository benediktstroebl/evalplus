```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The Python script provides a function `compare` which takes in two arrays `game` and `guess` and returns an array of the same length denoting how far off each guess was. If they have guessed correctly, the value is 0, and if not, the value is the absolute difference between the guess and the score. The function is designed to complete the task outlined in the prompt. It uses the zip function to iterate through the elements of both arrays and calculates the absolute difference between each element in the `game` and `guess` arrays. If the elements match, it sets the value to 0. Finally, it returns the resulting array of differences.