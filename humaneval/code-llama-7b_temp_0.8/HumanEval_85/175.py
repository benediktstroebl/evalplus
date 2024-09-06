
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst = [int(i) for i in lst.split(" ")]
    lst2 = []
    for i in range(len(lst)):
        if i % 2 == 0:
            lst2.append(lst[i])

    print(sum(lst2))

