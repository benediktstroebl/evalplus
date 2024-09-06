
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

    if not all(x % 2 == 0 for x in lst1):
        # 1. Find the first even element.
        for first_even_index in range(len(lst1)):
            if lst1[first_even_index] % 2 == 0:
                break

        # 2. Find the first uneven element.
        for first_uneven_index in range(len(lst2)):
            if lst2[first_uneven_index] % 2 != 0:
                break

        # 3. Exchange.
        lst1[first_even_index] = lst2[first_uneven_index]
        lst2[first_uneven_index] = lst1[first_even_index]

    if all(x % 2 == 0 for x in lst1):
        return "YES"
    else:
        return "NO"

