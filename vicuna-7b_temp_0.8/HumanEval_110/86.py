
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
    # if lst1 is even or lst2 is even return 'YES'
    if len(lst1) % 2 == 0 or len(lst2) % 2 == 0:
        return "YES"
    else:
        # check the difference between the two lists
        if len(lst1) > len(lst2):
            # if lst1 is bigger, add the last element of lst2 to lst1
            lst1.append(lst2.pop())
            # if lst2 is bigger, add the last element of lst1 to lst2
            lst2.append(lst1.pop())
        elif len(lst1) < len(lst2):
            # if lst1 is smaller, add the first element of lst2 to lst1
            lst1.insert(0, lst2.pop())
            # if lst2 is smaller, add the first element of lst1 to lst2
            lst2.insert(0, lst1.pop())
        # check the odd and even element of both list
        odd_lst1 = [x for x in lst1 if x % 2 != 0]
        odd_lst2 = [x for x in lst2 if x % 2 != 0]
        if odd_lst1 or odd_lst2:
            return "NO"
        else:
            # if all the elements of both lst1 and lst2 are even, return 'YES'
            return "YES"
