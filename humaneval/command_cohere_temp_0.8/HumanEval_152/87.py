```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```
This function takes two equal-length lists, game and guess, as arguments. It returns a list where each element is the difference between the corresponding elements in game and guess if the guess is incorrect, and 0 if the guess is correct. The result is returned as a list.

The solution utilizes Python's list comprehension and the zip() function to compare corresponding elements in the 'game' and 'guess' lists. For each pair of elements, it calculates the absolute difference if they don't match, and returns 0 if they do.