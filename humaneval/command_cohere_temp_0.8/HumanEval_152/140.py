```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns an array of the same length as the input arrays, where each element represents the difference between the corresponding elements in the `game` and `guess` arrays. If the guess was correct, the value is 0, and if not, the value is the absolute difference between the guess and the score. This function effectively compares the guesses against the actual results and returns an array reflecting how far off each guess was. 

Here is an example function call to `compare`:
```python
compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2])
```
This would return `[0, 0, 0, 0, 3, 3]`, as the corresponding elements in the two arrays are compared and the differences are calculated.