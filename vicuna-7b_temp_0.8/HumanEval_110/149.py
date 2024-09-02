
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
    # Check for empty lists
    if len(lst1) == 0 or len(lst2) == 0:
        return "NO"
    
    # Check if lst1 is already all even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Check if any element of lst1 can be exchanged with any element of lst2
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] != lst2[j]:
                return "NO"
    
    # Check if we can exchange any element of lst1 with lst2
    for i in range(len(lst1)):
        lst1[i], lst2[i] = lst2[i], lst1[i]
        if not all(num % 2 == 0 for num in lst1):
            return "NO"
        for j in range(len(lst1)):
            if lst1[j] != lst2[j]:
                return "NO"
        del lst1[i], lst2[i]
    
    return "YES"
