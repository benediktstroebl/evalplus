```python
def compare(game,guess):
    """
    Determine if a player's guesses are correct based on the game's scores.
    Return a numbers as a score corresponding to the number of matches the player got right.
    """
Each score is either 0 (guess was incorrect) or the absolute difference between the guess and the score.
    """
    example:
    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """

def test_compare():
    scores = [1,2,3,4,5,1]
    guess = [1,2,3,4,2,-2]
    correct_scores = [0]*len(scores)
    for i,score in enumerate(scores):
        correct_scores[i] = score - guess[i]
    matches = [True]*len(scores)
        for j,guess_score in enumerate(scores):
            if guess[j] == score:
                matches[j] = True
    return correct_scores

```
The provided code defines a function compare that determines if a player's guesses are correct based on the game's scores. The function returns an array of numbers corresponding to the number of matches the player got right. 

The test_compare function creates two arrays: scores and guess. Then, it loops through the each element in scores, comparing it with the corresponding element in guess. The function adds up the scores and guesses, setting the score to 0 if the guess is correct and subtracting the guess from the score if it is incorrect. The function stores the scores and guesses in a list called matches, where each index shows whether the guess was correct or not. 

Finally, the function returns the list of numbers corresponding to the number of matches the player got right.