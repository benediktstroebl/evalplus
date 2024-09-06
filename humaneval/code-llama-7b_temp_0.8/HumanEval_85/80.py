
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    # solution 1
    # lst = lst[::2]
    # return sum(lst)
    
    # solution 2
    return sum([e for i, e in enumerate(lst) if i % 2 == 1 and e % 2 == 0])



    # return sum([e for i, e in enumerate(lst) if i % 2 == 1 and e % 2 == 0])



    # # solution 3
    # result = 0
    # for i in range(1, len(lst), 2):
    #     result += lst[i]
    # return result




    # # solution 4
    # return sum(lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0)




    # # solution 5
    # return sum(lst[i] for i in range(1, len(lst), 2) if i % 2 == 1 and lst[i] % 2 == 0)



    # # solution 6
    # return sum([e for i, e in enumerate(lst) if i % 2 == 1 and e % 2 == 0])



    # # solution 7
    # return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])



    # # solution 8
    # return sum([e for i, e in enumerate(lst) if i % 2 == 1 and e % 2 == 0])



    # # solution 9
    # return sum([e for i, e in enumerate(lst) if i % 2 == 1 and e % 2 == 0])



    # # solution 10
    # return sum([e for i, e in enumerate(lst) if i % 2 == 1 and e % 2 == 0])



    # # solution 11
    # return sum([e for i, e in enumerate(lst) if i % 2 == 1 and e % 2 == 
