
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
    import random
    """
    # You should write your code here
    """
    # if sorted(lst1)==sorted(lst2):
    #     return "NO"
    # lst_1_even=[]
    # for n in lst1:
    #     if n%2==0:
    #         lst_1_even.append(n)
    # if sorted(lst2)==sorted(lst_1_even):
    #     return "YES"
    # else:
    #     return "NO"

    lst1.extend(lst2)
    lst2.extend(lst1)
    lst1.sort()
    lst2.sort()
    even_list=[]
    odd_list=[]
    for n in lst1:
        if n%2==0:
            even_list.append(n)
        else:
            odd_list.append(n)
    if sorted(lst2)==sorted(even_list):
        return "YES"
    else:
        return "
