
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
    # make two lists of even and odd numbers respectively
    evens = [e for e in lst1 if e%2==0]
    odds = [e for e in lst1 if e%2==1]

    # check if all elements in lst2 are even
    for num in lst2:
        if num%2==1:
            return "NO"

    # check if it's possible to swap a pair of elements between lst1 and lst2
    # to make lst1 contain all even numbers
    for i in range(len(evens)):
        # if lst1 has more evens than lst2, try to swap an even and an odd
        # number to make lst1 have one more even number than lst2
        if i < len(odds):
            if evens[i] + odds[i] <= lst2[i]:
                lst2[i] = lst2[i] - evens[i] + odds[i]
                evens[i] = lst1[i]
                lst1[i] = lst2[i]

        # if lst1 has more evens than lst2, swap an even and an odd number
        # to make lst1 have one more even number than lst2
        if len(lst2) <= i < len(odds):
            if evens[i] <= lst2[i]:
                lst2[i] = lst2[i] - evens[i] + odds[i]
                evens[i] = lst1[i]
                lst1[i] = lst2[i]

    # if lst2 has more evens than lst1, swap an even and an odd number
    # to make lst1 have one more even number than lst2
    for i in range(len(evens)):
        if len(lst1) <= i < len(odds):
            if evens[i] <= lst1[i]:
                lst1[i] = lst1[i] - evens[i] + odds[i]
                evens[i] = lst1[i]
                lst1[i] = lst1[i] - odds[i] + evens[i]

    
