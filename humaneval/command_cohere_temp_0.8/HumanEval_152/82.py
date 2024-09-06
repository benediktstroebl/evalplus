```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```
This Python script provides a function that takes in two lists, `game` and `guess`, and returns a list of the same length that denotes how far off each guess was from the corresponding score in the `game` list. The function works by using the list comprehension to go through each element in `game` and `guess` and checking if the elements are equal. If the elements are equal, the function returns a result of 0, if not it returns the absolute difference between the two lists.