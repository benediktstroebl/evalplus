```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns a list where each element corresponds to the absolute difference between the respective elements in the `game` and `guess` arrays, except when the elements in `guess` match the elements in `game`, in which case it returns 0. 

Here is an example of how to use the `compare` function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
print(compare(game, guess))
```
This will output:
```
[0, 0, 0, 0, 3, 3]
```
which indicates that the guesses were correct for the first 5 elements of the `game` array, but the last two elements were incorrect, with the guesses being 3 units off for the respective scores. 

Such evaluation allows for a concise and efficient verification of whether the guesses correspond to the provided scores and how far they were off in case of mismatch.