
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    # initialize variables
    even_nums = []

    for i in range(len(lst)):
        # check if i is even
        if i % 2 == 0:
            # add to even_nums
            even_nums.append(lst[i])

    total = 0
    for i in range(len(even_nums)):
        total += even_nums[i]

    return total
