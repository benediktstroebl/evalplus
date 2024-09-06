```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game,guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns a list where each element corresponds to the result of comparing the corresponding elements in the `game` and `guess` arrays. 

The function uses a list comprehension with a conditional check on each element of the corresponding elements in `game` and `guess`. If the elements are equal, it returns 0, otherwise, it returns the absolute difference between the two elements, effectively measuring the difference between the guess and the actual outcome of the games. 

Here is an example usage of this function:
```python
game_scores = [1, 2, 3, 4, 5, 1]
guess_scores = [1, 2, 3, 4, 2, -2]
print(compare(game_scores, guess_scores))
```
This will output:
```
[0, 0, 0, 0, 3, 3]
```

And another example:
```python
game_scores = [0, 5, 0, 0, 0, 4]
guess_scores = [4, 1, 1, 0, 0, -2]
print(compare(game_scores, guess_scores))
```
This will output:
```
[4, 4, 1, 0, 0, 6]
```