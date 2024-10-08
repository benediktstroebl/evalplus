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
    # Check if lst1 already has all even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the even numbers in lst2
    even_lst2 = [num for num in lst2 if num % 2 == 0]
    
    # Check if the sum of all even numbers in lst2 is greater than or equal to
    # the number of odd numbers in lst1
    if sum(even_lst2) >= len([num for num in lst1 if num % 2 == 1]):
        return "YES"
    
    return "NO"
