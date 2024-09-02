
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst.sort()
    even = [x for x in lst if x%2==0]
    odd = [x for x in lst if x%2!=0]
    return sum(even)

    # Write your code here.
