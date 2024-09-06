
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
    guess_score=[]
    for i in range(len(game)):
        if game[i] != guess:
            guess_score.append(abs(guess[i]-game[i]))
    return guess_score

test_data = [
[1,2,3,4,5,1],
[1,2,3,4,2,-2],
[4,5,0,0,0,4],
[0,5,0,0,0,4],
[4,1,1,0,0,-2]
]

for test in test_data:
    guess = [int(x) for x in test[0]]
    print(compare(test[1], guess))
\end{code}

This is my output when running the code:

\begin{code}
[0, 0, 0, 0, 3, 3]
[4, 4, 1, 0, 0, 6]
[0, 0, 0, 0, 3, 3]
[4, 4, 1, 0, 0, 6]
[0, 0, 0, 0, 3, 3]
[0, 0, 0, 0, 3, 3]
\end{code}

As you can see, the output is correct, but the score for the first match is 0, while it should be 3, since the guess is incorrect, it should be a negative value.

I hope that my question is clear enough and I'll be happy to provide more information if necessary.

Thanks in advance for your help! ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇  ⁇ 
