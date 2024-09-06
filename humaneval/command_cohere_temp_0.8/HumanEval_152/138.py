```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It iterates through corresponding elements of `game` and `guess` and calculates the absolute difference between them if the elements are different, indicating that the guess was incorrect. Conversely, if the elements are equal, it assigns a value of 0 to indicate a correct guess. The resulting list of differences or 0s is then returned as the output.