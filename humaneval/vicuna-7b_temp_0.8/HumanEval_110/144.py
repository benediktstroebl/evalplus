
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
    # Check if the input lists are non-empty
    if len(lst1) == 0 or len(lst2) == 0:
        return "NO"
    
    # Check if all the elements of lst1 are odd
    for num in lst1:
        if num % 2 != 0:
            return "NO"
    
    # Check if all the elements of lst2 are odd
    for num in lst2:
        if num % 2 != 0:
            return "NO"
    
    # Check if it is possible to exchange elements between the two lists
    # to make all the elements of lst1 to be even
    for i in range(len(lst1)-1):
        for j in range(i+1, len(lst2)):
            if lst1[i] == lst2[j]:
                # Exchange the elements
                lst1[i], lst2[j] = lst2[j], lst1[i]
                # Check if all the elements of lst1 are even
                for k in range(i+1, len(lst1)):
                    if (lst1[k] % 2) != 0:
                        return "NO"
                # If all the elements of lst1 are even, return "YES"
                return "YES"
    
    # If none of the above conditions are met, return "NO"
    return "NO"
