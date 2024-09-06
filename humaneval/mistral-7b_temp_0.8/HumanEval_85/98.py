
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Add your code here
    odd_list = []
    for i in range(0, len(lst), 2):
        if lst[i]%2 == 0:
            odd_list.append(lst[i])
    return sum(odd_list)
    # return even_list
