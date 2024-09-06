```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```
This function takes two equal-length lists, `game` and `guess`, where each element corresponds to the score of a match, and returns an array of the same length containing zero if the guess was correct, and the absolute difference between the guess and the score otherwise. Test cases are also provided within the code block to demonstrate the correct behavior of the function. 
The code adheres to Python's efficient list comprehension and chaining of expressions using the `if` statement.

Here is the full code block including tests:
```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]

# Tests:
game = [1,2,3,4,5,1]
guess = [1,2,3,4,2,-2]
assert compare(game, guess) == [0,0,0,0,3,3], "Correct result `[0,0,0,0,3,3]` for example 1"

game = [0,5,0,0,0,4]
guess = [4,1,1,0,0,-2]
assert compare(game, guess) == [4,4,1,0,0,6], "Correct result `[4,4,1,0,0,6]` for example 2"
```