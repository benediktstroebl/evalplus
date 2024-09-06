```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the result of a match, and returns a list where each element is the absolute difference between the guess and the score if the guess is incorrect, and 0 if the guess is correct. 

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
Which would be the appropriate solution for the given example. 

The function adheres to the problem statement and corresponding test cases. Feel free to test other scenarios to see how they correspond to the expected results.