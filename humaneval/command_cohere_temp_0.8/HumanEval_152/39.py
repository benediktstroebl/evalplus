```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```

The Python script provides a function `compare` which takes in two arrays `game` and `guess` and returns an array of the same length denoting how far off each guess was. If they have guessed correctly, the value is 0, and if not, the value is the absolute difference between the guess and the score. The function is designed to be self-contained and does not rely on any external variables or assumptions. It is important to note that the function assumes that the two arrays are already sorted in the correct order, which is mentioned in theBubble Sort code provided.