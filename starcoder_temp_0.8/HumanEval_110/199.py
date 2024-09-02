
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
    # Check if the lists are non-empty
    if not lst1 or not lst2:
        return 'NO'
    # Check if the lists have the same length
    if len(lst1)!= len(lst2):
        return 'NO'

    # Get the length of the lists
    length = len(lst1)
    # Store the even numbers of the first list
    even_lst1 = []
    for i in range(0, length):
        if lst1[i] % 2 == 0:
            even_lst1.append(lst1[i])

    # Count the number of even numbers in the second list
    count = 0
    for i in range(0, length):
        if lst2[i] % 2 == 0:
            count += 1

    # Check if the lists have the same number of even numbers
    if len(even_lst1)!= count:
        return 'NO'

    # Sort the list of even numbers in the first list
    even_lst1.sort()
    # Sort the list of even numbers in the second list
    lst2.sort()

    # Check if the lists have the same even numbers
    for i in range(0, length):
        if lst2[i]!= even_lst1[i]:
            return 'NO'

    return 'YES'

