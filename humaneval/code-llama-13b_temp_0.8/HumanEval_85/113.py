
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Your code here
    temp_list = []
    if not lst:
        return 0
    else:
        for idx, num in enumerate(lst):
            if idx % 2 == 1:
                temp_list.append(num)
        return sum(temp_list)

