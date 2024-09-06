```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game,guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the actual outcome of a match and the predicted outcome, respectively. It returns an array of the same length, where each element represents how far off the corresponding guess was from the actual outcome. If the guess was correct, the value is 0; otherwise, it is the absolute difference between the guess and the actual outcome. 

Here are some examples of input/output to illustrate how it works:
Example 1:
Input: ```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
```

Output:
```python
[0, 0, 0, 0, 3, 3]
```

Example 2:
Input: ```python
game = [0, 5, 0, 0, 0, 4]
guess = [4, 1, 1, 0, 0, -2]
```

Output:
```python
[4, 4, 1, 0, 0, 6]
```