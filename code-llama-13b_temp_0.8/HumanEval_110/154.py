
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
    # Keep track of the number of odds
    odd_number = 0
    # Make copies of the input lists
    list1 = lst1[:]
    list2 = lst2[:]
    # Iterate through list1, and if an element is odd, add 1 to the odd_number
    for num in list1:
        if num % 2 != 0:
            odd_number += 1
    # Iterate through list2, and if an element is odd, remove 1 from the odd_number
    for num in list2:
        if num % 2 != 0:
            odd_number -= 1
    # If there are an even number of odd numbers, return "YES"
    if odd_number % 2 == 0:
        return "YES"
    # Otherwise, return "NO"
    return "NO"
