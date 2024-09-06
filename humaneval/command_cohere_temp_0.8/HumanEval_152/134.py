```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The Python script provides a function `compare` which takes in two arrays `game` and `guess` and returns an array of the same length denoting how far off each guess was. If they have guessed correctly, the value is 0, and if not, the value is the absolute difference between the guess and the score. The function works by using the list comprehension to check for each element in `game` and `guess` if the values are not equal and returns the absolute difference between the two, else it returns a zero if the values are equal. 

This approach ensures that the returned array accurately reflects the deviation from the guesses to the corresponding scores of each match. 
The `compare` function works for the official problem statement test cases as well as the provided example:
```python
print(compare([1,2,3,4,5,1], [1,2,3,4,2,-2])) # [0,0,0,0,3,3]
print(compare([0,5,0,0,0,4], [4,1,1,0,0,-2])) # [4,4,1,0,0,6]
``` 

The output for both examples is: `[0, 0, 0, 0, 3, 3]` and `[4, 4, 1, 0, 0, 6]` respectively.  This demonstrates that the function `compare` correctly solves the problem as specified.  This script can be run directly or imported as a module in a larger Python project.