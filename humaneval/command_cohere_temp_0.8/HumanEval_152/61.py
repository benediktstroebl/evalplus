```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length lists, `game` and `guess`, where each element corresponds to a match result. It returns an list where each element is the absolute difference between the guess and the corresponding match result, if the guess is incorrect. Otherwise, the result is 0 if the guess is correct. 

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