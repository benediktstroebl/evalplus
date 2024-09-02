
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
    # Your code here
    # loop through lst1 and lst2 and swap elements
    # loop through lst1 and check for elements that are even
    # if any element is not even, return NO
    # else return YES

    temp1 = []
    temp2 = []
    while lst1 or lst2:
        while lst1:
            if lst1[0] % 2 == 0:
                temp1.append(lst1.pop(0))
            else:
                lst1.pop(0)
                break
        while lst2:
            if lst2[0] % 2 == 0:
                temp2.append(lst2.pop(0))
            else:
                lst2.pop(0)
                break

    if temp1 == temp2:
        return "YES"
    else:
        return "NO"

