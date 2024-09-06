
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
    # TODO: Write your solution here
    # pairings = zip(lst1, lst2)
    # new_lst = [(item[0], item[1]) for item in pairings]
    # new_lst = new_lst[0]

    # print(new_lst)
    # for item in new_lst:
    #     print(item)

    lst1_even = [num for num in lst1 if num % 2 == 0]
    lst1_odd = [num for num in lst1 if num % 2 != 0]

    lst2_even = [num for num in lst2 if num % 2 == 0]
    lst2_odd = [num for num in lst2 if num % 2 != 0]

    if len(lst1_even) == len(lst2_even):
        return "YES"
    elif len(lst1_odd) == len(lst2_odd):
        return "YES"
    else:
        return "NO"

