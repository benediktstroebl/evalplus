
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
    # for each number in lst1, if it is odd, check if there is a number in lst2
    # which is the same number but is even, if so, exchange them

    def is_even(n):
        return n % 2 == 0

    def is_odd(n):
        return n % 2 != 0

    if len(lst1) != len(lst2):
        return "NO"

    # verify that each number in lst1 is odd
    for n in lst1:
        if is_even(n):
            return "NO"

    # verify that each number in lst2 is odd
    for n in lst2:
        if is_even(n):
            return "NO"

    # loop through each number in lst1
    # if number is odd, find the index of the number in lst2,
    # if number in lst2 is odd, exchange numbers at both indices
    # repeat until lst1 is empty
    index = 0
    while lst1:
        n = lst1.pop()
        if is_odd(n):
            while lst2:
                m = lst2.pop()
                if is_odd(m) and m == n:
                    lst1.append(m)
                    lst2.append(n)
                    break

    return "YES" if not lst2 else "NO"

