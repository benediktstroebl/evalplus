
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

    # heuristic: on each step, look for a pair of elements that sum up to an even number
    # remove them from both lists, and add them to the list of exchanges
    # repeat until one of the lists is empty
    # if lst1 is empty, return "NO"
    # if lst1 has only even numbers, return "YES"

    # create sets for quick lookup
    s1 = set(lst1)
    s2 = set(lst2)
    exchanges = []
    while len(lst1) > 0:
        for e1 in lst1:
            # find e2 in s2 that sums up to an even number with e1
            for e2 in s2:
                if e1 + e2 % 2 == 0:
                    exchanges.append((e1, e2))
                    s1.remove(e1)
                    s2.remove(e2)
                    lst1.remove(e1)
                    lst2.remove(e2)
                    break
            # if we found a match for e1, don't look further
            if e1 not in s1:
                break
        else:
            # if we did not find any match, return "NO"
            return "NO"
    return "YES"
