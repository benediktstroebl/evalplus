
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

    odd = False
    lst1_copy = lst1[:]
    lst2_copy = lst2[:]
    for num1 in lst1_copy:
        if num1 % 2 == 0:
            lst1.remove(num1)
            lst2.append(num1)
        else:
            odd = True
    for num2 in lst2_copy:
        if num2 % 2 == 0:
            lst2.remove(num2)
            lst1.append(num2)
        else:
            odd = True
    if len(lst1) == 0:
        return "YES"
    if odd:
        return "NO"
    return exchange(lst1, lst2)
