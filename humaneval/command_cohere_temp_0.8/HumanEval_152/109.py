```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The solution works by using Python's list comprehension and short-circuit evaluation to create a new list where each element is the absolute difference between the corresponding elements in `game` and `guess` if they are different, and 0 if they are equal. 

This behaviour is denoted by the expression `abs(x-y) if x != y else 0`. Short-circuit evaluation will ensure that the condition `x != y` is only evaluated when the outcome of the expression is dependent on it, namely when `x` and `y` are different. Hence, the expression as a whole will return the absolute difference between the two numbers when they are different, and `0` when they are equal. 

The expression is placed inside a list comprehension that iterates over pairs of corresponding elements in `game` and `guess`. The resulting list will be returned as the output of the function. 

The code is encapsulated in a self-contained function `compare` with two parameters `game` and `guess`. These are meant to be two lists of equal length that contain the scores of a number of matches and a person's guesses of the same scores respectively. The function returns a list of the same length as the two input lists, where each element is the numerical difference between the person's guess and the actual score, or 0 if the person guessed correctly. 

You can use this function to test the behaviour against test cases.