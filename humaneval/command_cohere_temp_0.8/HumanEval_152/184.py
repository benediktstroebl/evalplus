```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```
This function takes two equal-length lists, game and guess, as arguments. It returns a list where each element is the absolute difference between the corresponding elements in game and guess if they don't match, and 0 if the guess was correct. The list is returned after iterating through each element using the zip function, which takes two iterables and returns a tuple of corresponding elements. This allows us to easily compare and calculate the differences for each pair of elements.