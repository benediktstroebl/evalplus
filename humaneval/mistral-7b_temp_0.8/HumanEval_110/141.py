
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
    # Write your code here
    # start by checking that the second list contains an odd number
    for x in lst2:
        if x % 2 != 0:
            return "NO"
    # now check that the second list contains a number greater than the first list
    for x in lst2:
        if x > max(lst1):
            return "NO"
    # now we know that the second list can supply the necessary numbers
    # first get the odd numbers in the first list
    odd = [x for x in lst1 if x % 2 != 0]
    # now get the even numbers in the first list
    even = [x for x in lst1 if x % 2 == 0]
    # remove the odd numbers from the first list
    lst1 = [x for x in lst1 if x not in odd]
    # now get the even numbers in the second list
    even2 = [x for x in lst2 if x % 2 == 0]
    # remove the even numbers from the second list
    lst2 = [x for x in
