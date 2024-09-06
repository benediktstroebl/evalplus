```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```
This Python script defines a function called `compare` which takes two arrays, `game` and `guess`, as input. It compares the elements of these arrays, which represent game scores and user guesses respectively, and calculates the absolute difference between corresponding elements if they don't match. If the elements match, it assigns a value of 0 to the corresponding result. The function then returns a list of these result values, essentially indicating how far off each guess was from the actual scores. The output list will contain 0 at positions where the guess was correct, and the absolute difference at positions where the guess was incorrect. 

Here's an example to further illustrate its usage: 
```python
print(compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2,-2]))
```
This would print: 
```
[0, 0, 0, 0, 3, 3]
```
Here's another example:
```python
print(compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0,-2]))
```
This would give the following output: 
```
[4, 4, 1, 0, 0, 6]
```