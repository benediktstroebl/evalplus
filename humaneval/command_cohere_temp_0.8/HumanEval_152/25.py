```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the result of a match, and returns a new array where each element represents how far off the corresponding guess was from the actual result. If the guess was correct, the result is 0, and otherwise, it's the absolute difference between the guess and the actual result. 

Here is an example usage of the function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
print(compare(game, guess))
```
This will output:
```
[0, 0, 0, 0, 3, 3]
```
The result shows that the guess array has some correct guesses (at indices 0, 1, 2, 4) with a deviation of 0 for each of these, indicating the person guessed correctly. At index 3, however, the guess was 2, but the actual result was 5, resulting in a deviation of 3.