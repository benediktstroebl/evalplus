```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns a list where each element represents the difference between the corresponding elements in the `game` and `guess` arrays, or 0 if the guess was correct. To achieve this, the function uses Python's `zip` function to iterate through corresponding elements of both arrays and calculates the absolute difference, `abs`, between them. The result is a list that shows how far off each guess was from the actual results.