
def compare(game,guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    # This is the correct approach
    guess_list = [int(i) for i in guess.split(",")]
    score_list = [int(i) for i in game.split(",")]

    score_dict = {int(i): 0 for i in score_list}
    guess_dict = {int(i): guess_list.index(i) for i in score_list}

    correct_guesses = [i for i, v in score_dict.items() if v == 2]
    correct_indexes = [guess_dict[i] for i in correct_guesses]
    correct_scores = score_list[correct_indexes]

    error_list = [abs(c - s) for c, s in zip(correct_guesses, score_list)]

    return error_list
