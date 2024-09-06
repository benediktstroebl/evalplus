```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the actual outcome of a match and the guessed outcome, respectively. It returns an array of the same length, where each element is the absolute difference between the guess and the score if the guess was incorrect, and 0 if the guess was correct. 

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
Which indicates that the guesses for the second, third, fourth, and fifth matches were incorrect by 3, and the guess for the first and last matches were correct. 

Such a simple algorithm is both efficient in terms of time and space complexity, and it's straightforward to implement, making it a great solution for this particular challenge.