```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns a list where each element corresponds to the result of comparing the corresponding elements in the `game` and `guess` arrays. 

The function evaluates whether each pair of elements in `game` and `guess` arrays are identical. If so, it returns 0, indicating an accurate guess. Otherwise, it calculates the absolute difference between the two elements, which reflects the discrepancy between the guess and the actual outcome. 

Here is an example usage of this function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
print(compare(game, guess))
```
This will output:
```
[0, 0, 0, 0, 3, 3]
``` 

Another example:
```python
game = [0, 5, 0, 0, 0, 4]
guess = [4, 1, 1, 0, 0, -2]
print(compare(game, guess))
```
This will output:
```
[4, 4, 1, 0, 0, 6]
``` 

These examples demonstrate how the `compare` function evaluates and returns the results of the comparison.