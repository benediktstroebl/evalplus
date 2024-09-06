
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    odd_nums = [i for i in lst if i % 2 == 0]
    odd_indices = [lst.index(i) for i in odd_nums]
    odd_indices.sort()
    return sum(odd_nums)

