
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    """
    Write code to add up the even elements that are at odd indices.
    For example, if the input list is [4, 2, 6, 7], you should return the list [6, 7].

    Tips:
        You can use the following functions on lists in Python:
        - len(lst): returns the length of the list
        - lst[i]: returns the element at index i in the list
        - lst[i:j]: returns a list consisting of the elements of the list from index i to index j-1
    """
    # your code here
    odd = 0
    for i in range(len(lst)):
        if i%2==1:
            odd = lst[i]
    return odd
