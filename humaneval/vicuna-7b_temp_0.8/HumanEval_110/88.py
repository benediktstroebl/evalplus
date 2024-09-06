
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
    def check(lst):
        # Check if the length of lst is odd
        if len(lst) % 2 == 1:
            return False
        # Check if all the elements of lst are even
        for element in lst:
            if element != 0:
                return False
        return True

    lst1 = sorted(lst1)
    lst2 = sorted(lst2)

    while lst1 and lst2:
        if check(lst1[-1]):
            lst1.pop()
            lst2.append(lst1[-1])
            break
        if check(lst2[-1]):
            lst2.pop()
            lst1.append(lst2[-1])
            break
        elif lst1[-1] < lst2[-1]:
            lst1.pop()
            lst2.append(lst1[-1])
            break
        else:
            lst2.pop()
            lst1.append(lst2[-1])
            break

    return check(lst1)
