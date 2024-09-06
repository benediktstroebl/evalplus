```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It returns a list where each element corresponds to the result of comparing the corresponding elements in the `game` and `guess` arrays. 

The function uses a list comprehension with a conditional check on each pair of corresponding elements from the `game` and `guess` arrays. When the elements match, the result is 0, and when they don't, the result is the absolute difference between the two elements. 

Here is an example:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
result = compare(game, guess)
print(result)
```
Which would print:
```
[0, 0, 0, 0, 3, 3]
```
In this example, the result list reflects the absolute difference between the guess and the score for each corresponding element that didn't match, and 0 for each correctly guessed element. 
The conditional check and zipper method in the `compare` function ensure that the result list accurately reflects the user's instructions in the prompt.