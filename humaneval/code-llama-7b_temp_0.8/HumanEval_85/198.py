
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    # TODO: Write your solution here
    sum = 0
    for i in range(len(lst)):
        if i % 2 == 1:
            sum += lst[i]
    return sum

