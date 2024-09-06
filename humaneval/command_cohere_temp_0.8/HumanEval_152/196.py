```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the actual result of a match and the predicted result by a person, respectively. It returns an array of the same length indicating how far off each guess was. If the guess matches the actual result, it returns `0`, otherwise, it returns the absolute difference between the guess and the actual result. 

Here is an example usage of the function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
result = compare(game, guess)
print(result) 
 # Output: [0, 0, 0, 0, 3, 3]
```
This will output `[0, 0, 0, 0, 3, 3]`, where the person correctly guessed the outcome of 4 matches, and the result indicates how many points off they were for the remaining matches. 
Here is another example:
```python
game = [0, 5, 0, 0, 0, 4]
guess = [4, 1, 1, 0, 0, -2]
result = compare(game, guess)
print(result)
 # Output: [4, 4, 1, 0, 0, 6]
```
This will output `[4, 4, 1, 0, 0, 6]`, where the person missed the mark on all matches, and the result indicates the absolute difference between the guess and the actual outcome. Folks, it's showdown time! Do you want to join me in celebrating this solution?