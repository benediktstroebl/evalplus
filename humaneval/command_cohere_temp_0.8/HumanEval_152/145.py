```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns a list where each element represents the difference between the corresponding elements in the `game` and `guess` arrays, or 0 if the guess was correct. This is done using the `zip` function to iterate through corresponding elements of both arrays and calculate the absolute difference, this difference is then returned for each element unless the guess was correct in which case 0 is returned.