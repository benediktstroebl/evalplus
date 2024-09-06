```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length lists, `game` and `guess`, as arguments. It returns a list where each element is the absolute difference between the corresponding elements in `game` and `guess` if they don't match, and 0 if the guess was correct. The function uses the `zip` function to iterate through corresponding elements of both lists. Finally, the `abs` function is used to calculate the absolute difference between the elements when they don't match the expected outcome.