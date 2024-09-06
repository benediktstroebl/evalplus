```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the score of a match, and returns an array of the same length containing the absolute difference between the guess and the score if the guess is incorrect, and 0 if the guess is correct. 

The tests this function passes are:
```python
def test_compare():
    # Test Case 1
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 2, -2]
    expected = [0, 0, 0, 0, 3, 3]
    result = compare(game, guess)
    assert result == expected

    # Test Case 2
    game = [0, 5, 0, 0, 0, 4]
    guess = [4, 1, 1, 0, 0, -2]
    expected = [4, 4, 1, 0, 0, 6]
    result = compare(game, guess)
    assert result == expected

test_compare()
``` 
The code passes these tests, confirming that it correctly solves the problem. A user can incorporate this code into their solution and assert its correctness against the test cases provided.