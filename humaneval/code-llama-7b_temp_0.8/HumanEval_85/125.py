
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_odd = [i if lst[i] % 2 == 0 else 0 for i in range(len(lst))]
    even_odd_sum = [even_odd[i] + even_odd[i + 1] for i in range(0, len(lst), 2)]
    return sum(even_odd_sum)
