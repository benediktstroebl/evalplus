```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```

The Python script provides a function named `compare` which takes two arrays, `game` and `guess`, as input. It aims to determine how far off each guess in the `guess` array is from the corresponding score in the `game` array. 

The function is crafted using a list comprehension, which iterates through pairs of corresponding elements (scoring and guessing) from the `game` and `guess` arrays. It employs the `zip` function to seamlessly combine the two arrays for this element-by-element comparison.

For each pair, it calculates the absolute difference between the scores and guesses, using the `abs` function. However, if the guess correctly predicts the score (meaning they are equal), it assigns a value of 0 to the result, implying a correct guess. 

Finally, the function constructs and returns a new array, `result`, which contains the computed values for each pair, representing how far off each guess was from the corresponding score. 

Example usage:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
result = compare(game, guess)
print(result)  # Output: [0, 0, 0, 0, 3, 3]
``` 

This will output `[0, 0, 0, 0, 3, 3]`, where the first element (at index 0) has a difference of 0, indicating a correct guess, while the last element (at index 5) has a difference of 3, indicating that the guess was off by 3 from the actual score. 

The given example and the provided code entirely adhere to the problem statement, ensuring accurate determination of how far off each guess is from the corresponding score, while also correctly identifying correct guesses.