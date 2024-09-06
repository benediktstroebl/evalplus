```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The Python script provides a function `compare` which takes in two arrays `game` and `guess` and returns an array of the same length denoting how far off each guess was. If they have guessed correctly, the value is 0, and if not, the value is the absolute difference between the guess and the score. The function works by using Python's `zip` function to iterate through each element in `game` and `guess` simultaneously. It then checks if the values are not equal and returns the absolute difference between the two integers, or else returns 0 if the values are equal. 

This solution works for the given test cases and produces the correct results based on the problem statement.