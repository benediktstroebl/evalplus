
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_lst = [i for i in lst if i % 2 == 0]
    lst = [i for i in lst if i % 2 == 1]
    return [x+y for x,y in zip(even_lst,lst)]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
