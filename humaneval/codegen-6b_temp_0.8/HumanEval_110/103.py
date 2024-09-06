
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
    def exchange_helper(l1, l2, exchange_list):
        if l1 == []:
            return "YES"
        elif l2 == []:
            return "NO"
        else:
            exchange_list.append(l1[0])
            exchange_list.append(l2[0])
            return exchange_helper(l1[1:], l2[1:], exchange_list)

    return exchange_helper(lst1, lst2, [])
