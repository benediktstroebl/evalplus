```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```

The Python script provides a function `compare` which takes in two arrays `game` and `guess` and returns an array of the same length denoting how far off each guess was. If they have guessed correctly, the value is 0, and if not, the value is the absolute difference between the guess and the score. The function works by using the zip function to iterate through each element of both arrays and calculating the absolute difference between the two values. Note that the function assumes that the two arrays are of equal length. Would you like to know more about the code? 

Any questions or doubts about the problem, the provided code, or anything else you'd like me to clarify? Feel free to ask, and I'll do my best to help.