```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game,guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns an array of the same length as these inputs, where each element represents the difference between the corresponding elements in the `game` and `guess` arrays. If the guess was correct, the result is 0, otherwise, it is the absolute difference between the guess and the score.

Here is an example usage of this function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
print(compare(game, guess))
```
This will output:
```python
[0, 0, 0, 0, 3, 3]
```
The output is an array where each element represents the difference between the corresponding elements in the `game` and `guess` arrays. If the guess was correct, the result is 0, and if not, it is the absolute difference between the guess and the score.  In this example, the result array would be [0, 0, 0, 0, 3, 3] since the guesses were correct for the first 3 elements, and then missed by 3 for the last 3 elements.