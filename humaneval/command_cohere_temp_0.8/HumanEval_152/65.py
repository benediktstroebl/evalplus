```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```
This Python script defines a function named `compare` which takes two arrays, `game` and `guess`, as input. It returns an array of the same length as these inputs, where each element represents the difference between the corresponding elements of `game` and `guess`. If the guess matches the game result, it returns `0`, otherwise it returns the absolute difference between the guess and the score. This function serves the purpose of checking and comparing guesses against the actual results of a series of matches, as described in the Problem Statement. 

This script adheres to Python's syntax and conventions, including using indentation to define code blocks and using parentheses and commas to maintain proper syntax clarity. Additionally, it is optimized for readability and adheres to coding best practices.