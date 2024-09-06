```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game,guess)]
```
This Python script defines a function named `compare` which takes two arrays, `game` and `guess`, as input. It returns an array of the same length as these inputs, where each element represents the difference between the corresponding elements in the `game` and `guess` arrays. If the guess was correct, the result is 0, otherwise, it is the absolute difference between the guess and the score.

Here is an example usage of this function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
result = compare(game, guess)
print(result)  # Output: [0, 0, 0, 0, 3, 3]
```
This will produce the desired output of `[0, 0, 0, 0, 3, 3]`. 

The provided code is concise and efficient, providing a standalone solution to the problem as required. It achieves this without resorting to any global variables, making it reusable and maintaining the rigidity of the function, in line with the principle of atomicity in functional programming. 

Also, the code employs list comprehension, a potent Python construct for manipulating lists, to compute the differences, lending an elegant and streamlined appearance to the code.