
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
    # determine if lst1 contains any odd numbers
    has_odd = False
    for num in lst1:
        if num % 2 != 0:
            has_odd = True
            break
    # if lst1 has odd numbers, try to exchange with lst2
    if has_odd:
        # determine if lst2 has even numbers
        for num in lst2:
            if num % 2 == 0:
                lst1[lst1.index(num)] = lst2[lst2.index(num)]
                lst2[lst2.index(num)] = num
        # check if lst1 contains any odd numbers again
        has_odd = False
        for num in lst1:
            if num % 2 != 0:
                has_odd = True
                break
        # if lst1 still has odd numbers, it is not possible to make lst1 all even
        if has_odd:
            return "NO"
        else:
            return "YES"
    else:
        return "NO"

