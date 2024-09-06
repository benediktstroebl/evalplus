
def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    # Create an empty list to store even numbers
    even_lst = []
    
    # Iterate through each element in the first list
    for x in lst1:
        # If the element is even, append it to the even_lst
        if x % 2 == 0:
            even_lst.append(x)
        else:
            # If the element is odd, append it to the odd_lst
            odd_lst.append(x)
    
    # If the even_lst is empty, return "NO"
    if len(even_lst) == 0:
        return "NO"
    
    # If the even_lst is not empty, return "YES"
    return "YES"
