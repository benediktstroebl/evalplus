
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
    # 1. Go through all the elements of the list, 
    # and if an element is not even, search for it in the second list.
    # 2. If found, check if its index in the second list is even.
    # If so, exchange them and continue with the first list.
    # 3. If the element is not found, or its index in the second list is odd, 
    # then this pair of lists cannot lead to an answer and we should return "NO"
    for idx1 in range(len(lst1)):
        if lst1[idx1] % 2 != 0:
            found = False
            for idx2 in range(len(lst2)):
                if lst2[idx2] == lst1[idx1]:
                    if idx2 % 2 == 0:
                        lst1[idx1], lst2[idx2] = lst2[idx2], lst1[idx1]
                        found = True
                        break
                    else:
                        return "NO"
            if not found:
                return "NO"
    return "YES"
