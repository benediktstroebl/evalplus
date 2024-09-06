```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```
This function takes two equal-length lists, game and guess, as arguments. It returns a list where each element is the absolute difference between the corresponding elements in game and guess if they are different, and 0 if the guess was correct. The list is constructed using the zip command which iterates over the corresponding elements in both lists at the same time. The abs function is used to get the absolute difference between the corresponding elements. 

Here is an example usage of the function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
print(compare(game, guess))
```
This would print:
```
[0, 0, 0, 0, 3, 3]
```
which indicates that the guesses were correct for the first 4 elements, and the differences for the last two elements. 

Here is another example:
```python
game = [0, 5, 0, 0, 0, 4]
guess = [4, 1, 1, 0, 0, -2]
print(compare(game, guess))
```
This would print:
```
[4, 4, 1, 0, 0, 6]
```
which indicates that the guess was incorrect by 4 units for the first element, and the rest were correct.