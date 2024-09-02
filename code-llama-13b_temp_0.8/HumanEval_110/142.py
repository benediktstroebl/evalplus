
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

    # check if all lst1 has only even numbers
    if all(num % 2 == 0 for num in lst1):
        return 'YES'
    # if not, check if lst2 has odd number
    elif any(num % 2 == 1 for num in lst2):
        return 'NO'
    # if not, then the following exchange will make lst1 has only even numbers
    else:
        # loop over each number in lst2
        for i in lst2:
            # check if lst1 has the same number as lst2
            if i in lst1:
                # remove the number in lst1
                lst1.remove(i)
                # add the number into lst2
                lst2.append(i)
                # check if lst1 has only even numbers
                if all(num % 2 == 0 for num in lst1):
                    return 'YES'

    return 'NO'
