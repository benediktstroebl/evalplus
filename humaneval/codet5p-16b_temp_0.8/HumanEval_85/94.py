
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    even_odd = [lst[x] for x in range(len(lst)) if x % 2 == 1]
    print(even_odd)
    return sum([i for i in even_odd if i % 2 == 0])

