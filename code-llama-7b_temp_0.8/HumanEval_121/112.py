
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    odds = list(filter(lambda x: x % 2 != 0, lst))
    even_positions = list(map(lambda x: x if x % 2 == 0 else None, lst))
    even_odds = []
    for idx in range(len(even_positions)):
        if even_positions[idx] and even_positions[idx] in odds:
            even_odds.append(even_positions[idx])
    
    return sum(even_odds)

