```python
def compare(game, guess):
    """Return an array showing the difference between the guess and the actual game score.
    If the guess is correct, the value is 0.
    """
    result = []
    for i in range(len(game)):
        result.append(abs(game[i] - guess[i]))
    return result
```