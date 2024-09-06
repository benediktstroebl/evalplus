```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It compares the elements of the two arrays element-wise, calculating the absolute difference between each element if they don't match, and 0 if the guess was correct. The result is a list of absolute differences or 0s, accordingly. The function is designed to solve the problem statement provided in the prompt, which asks to return an array of the same length denoting how far off each guess was, where the result is 0 for correct guesses and the absolute difference for incorrect ones.