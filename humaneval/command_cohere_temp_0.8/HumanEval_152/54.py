```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns an array of the same length as the input arrays, where each element represents the difference between the corresponding elements in the `game` and `guess` arrays. If the guess is correct, the value is 0, otherwise, it is the absolute difference between the guess and the score.

Here is an example of how to use the `compare` function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
print(compare(game, guess))
```
This will output:
```python
[0, 0, 0, 0, 3, 3]
```

And another example:
```python
game = [0, 5, 0, 0, 0, 4]
guess = [4, 1, 1, 0, 0, -2]
print(compare(game, guess))
```
This will output:
```python
[4, 4, 1, 0, 0, 6]
```