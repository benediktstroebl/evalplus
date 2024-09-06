
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even = []
    for x in lst:
        if x % 2 == 0:
            even.append(x)

    # print(even)
    odd = []
    for n in lst:
        if n % 2 != 0:
            odd.append(n)
    # print(odd)
    return even+odd

