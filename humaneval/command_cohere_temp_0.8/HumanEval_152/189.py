```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```
This Python script provides a function that takes in two lists, `game` and `guess`, and returns a list of absolute differences between corresponding elements in `game` and `guess`, or 0 if the corresponding elements are equal. The absolute differences represent the error between the guesses and the actual results of the games, and the function returns these errors for each game.  The function is designed to work correctly and efficiently to solve the problem statement provided. 

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
which indicates that the guesses were correct for the first 5 indices, and the differences for the last two indices, with differences of 3.