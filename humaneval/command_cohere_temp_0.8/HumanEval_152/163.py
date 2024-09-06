```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```
This Python script provides a function that takes two lists, namely `game` and `guess`, and returns a list of absolute differences between corresponding elements in `game` and `guess`, or 0 if the elements are equal. The absolute differences denote how far off each guess in `guess` was from the corresponding scores in `game`. The function is designed to process matched pairs of elements efficiently using Python's list comprehension and zipping capabilities, making it suitable for handling large datasets.