```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The solution works by using Python's list comprehension and zipper to compare in parallel each element of the `game` and `guess` arrays. In case they differ, the resulting element of the new array is the absolute difference between the two, and if they are equal, it is 0. 

Such solutions demonstrate the power of Python and its elegant and simple one-liner solutions for array manipulations and transformations. 

This approach allows for a concise and readable solution to the problem, as the logic for comparing each element in parallel and returning the result is encapsulated within the list comprehension. 

To test this, one could create a simple module with a few test cases to see if the function correctly returns the offness of each guess, or correctly returns 0 if the guess was correct: 

```python
def test_compare():
    # Correct Guess
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

    # Incorrect Guess
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

    # Mixed Guess
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 5, 1]) == [0, 0, 0, 0, 0, 0]

    # All Guess
    assert compare([0, 0, 0, 10, 30, 40], [0, 0, 0, 10, 30, 40]) == [0, 0, 0, 0, 0, 0]
``` 

The `test_compare` function provides test cases that cover all possible scenarios for the `compare` function and verifies that the expected output is returned for each case.