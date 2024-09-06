```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game,guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the score of a match, and returns an array of the same length containing the absolute difference between the guess and the score if the guess is incorrect, and 0 if the guess is correct. 

The tests this function passes are:
```python
def test_compare():
    # First example:
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

    # Second example:
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

    # Edge case:
    assert compare([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0]

    # Edge case:
    assert compare([-1, 2, 3, 4, 5, 1], [-1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

test_compare()
```

Make sure to install the necessary dependencies (`markdown`, `pytest` and `pytest-markdown`) to run the test file above, and you can verify the correctness of the function by running the test file.