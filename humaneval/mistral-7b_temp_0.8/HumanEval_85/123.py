
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    odd_index = 0
    even_sum = 0
    for i in range(len(lst)):
        if i%2 == 0:
            even_sum += lst[i]
        if i%2 == 1 and lst[i]%2 == 0:
            odd_index = i
    return even_sum + lst[odd_index]
