
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

    # 1.1 두 배열이 같은 길이이므로, 2개의 배열을 차례대로 반복
    for i in range(len(game)):
        # 1.2 두 배열의 값을 비교하여, 배열의 길이가 같다면 베스트셀러는 그냥 빈 배열을 반환
        if game[i] == guess[i]:
            print(i,game[i],guess[i])

            pass
        # 1.3 그렇지 않다면 2개의 값을 더한 후, 빈 배열을 반환
        else:
            print(i,game[i],guess[i])

            # compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
            # compare([0,
