
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
    # Initialize the answer
    answer = "YES"
    # Check if both lists are non-empty
    if len(lst1) == 0 or len(lst2) == 0:
        return "NO"
    # If the lists are not of the same length, return "NO"
    if len(lst1)!= len(lst2):
        return "NO"
    # Iterate over the lists and count the number of odd numbers
    odd_count = 0
    for num in lst1:
        if num % 2!= 0:
            odd_count += 1
    # If the number of odd numbers in the first list is not equal to the
    # number of even numbers in the second list, return "NO"
    if odd_count!= len(lst2) - odd_count:
        return "NO"
    # If the lists contain only even numbers, return "YES"
    for num in lst1:
        if num % 2!= 0:
            return "NO"
    return answer
