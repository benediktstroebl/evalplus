
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """


    odd_index = [i for i,x in enumerate(lst) if i % 2 == 1]
    print(odd_index)
    even_val = [x for i,x in enumerate(lst) if i % 2 == 0]
    print(even_val)
    #if lst[i] % 2 == 0:
    #    new_list.append(lst[i])
    #return new_list

