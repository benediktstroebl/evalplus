
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
    # Elegant Solution
    # Two pointers
    # O(n) time | O(1) space

    # Iterate from the start of lst1 and lst2
    # As long as both are not at the end of their list and the evenness of the
    # current value is the same, move both pointers forward
    # if they are not at the end of their list and the evenness of the current
    # value is different, swap the current value between lst1 and lst2
    # If one of the lists reaches the end of its list before the other, return
    # "NO"
    # If neither of the lists reach the end of their list before the other, return
    # "YES"
    even = True
    evenness = None
    # Iterate from the start of lst1 and lst2
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        # As long as both are not at the end of their list and the evenness of the
        # current value is the same, move both pointers forward
        if lst1[i] % 2 == even and lst2[j] % 2 == even:
            i += 1
            j += 1
        # If they are not at the end of their list and the evenness of the current
        # value is different, swap the current value between lst1 and lst2
        else:
            lst1[i], lst2[j] = lst2[j], lst1[i]
            even = not even
            # If one of the lists reaches the end of its list before the other, return
            # "NO"
            if even != evenness:
                return "NO"
            # If neither of the lists reach the end of their list before the other, return
            # "YES"
            evenness = not evenness
        i += 1
        j += 1

    return "YES"

