
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    if len(lst) < 1:
        return 0

    # lst = [4, 2, 6, 7]
    # lst.index(4) = 0
    # lst.index(2) = 1
    # lst.index(6) = 2
    # lst.index(7) = 3


    # even_at_odds = [lst[lst.index(i)] for i in lst if i % 2 == 0 and lst.index(i) % 2 != 0]

    # if even_at_odds == []:
    #     return 0
    # else:
    #     return sum(even_at_odds)

    # lst = [4, 2, 6, 7]
    #
    # even_at_odds = []
    # for i in lst:
    #     if i % 2 == 0:
    #         if lst.index(i) % 2 != 0:
    #             even_
