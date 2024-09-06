```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game,guess)]
```
This function takes two equal-length lists, `game` and `guess`, where each element corresponds to a match result. It returns an array of the same length containing zero if the guess was correct for that match, and the absolute difference between the two lists otherwise. 

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

Such a solution is among the most efficient and readable, employing list comprehension and zip to iterate through the elements efficiently and return the result as required.