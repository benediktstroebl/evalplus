
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
    # def even(number):
    #     if number % 2 == 0:
    #         return True
    #     else:
    #         return False

    # if not even(lst1[-1]):
    #     if even(lst2[0]):
    #         return "YES"
    #     else:
    #         return "NO"
    # else:
    #     if even(lst2[-1]):
    #         return "YES"
    #     else:
    #         return "NO"

    lst1_even = [number for number in lst1 if number % 2 == 0]
    lst1_odd = [number for number in lst1 if number % 2 != 0]
    lst2_even = [number for number in lst2 if number % 2 == 0]
    lst2_odd = [number for number in lst2 if number % 2 != 0]
    if not lst1_even and lst1_odd and lst2_odd:
        return "NO"
    else:
        return "YES"

