
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    evens = [i for i, x in enumerate(lst) if x % 2 == 0]
    odds = [i for i, x in enumerate(lst) if x % 2 == 1]

    evens_at_odds = [lst[i] for i in zip(evens, odds) if i[0] < i[1]]
    return sum(evens_at_odds)

