
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    even_sum = 0
    odd_sum = 0
    for i,v in enumerate(lst):
        if i % 2 == 0:
            even_sum += v
        else:
            odd_sum += v
    return even_sum - odd_sum
