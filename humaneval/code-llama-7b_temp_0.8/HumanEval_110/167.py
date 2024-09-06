
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
    # Your code here
    # uncomment the next line when you are done
    #raise NotImplementedError()

    even = []
    odd = []

    for num in lst1:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    print("even:", even, "odd:", odd)
    for num in lst2:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    print("even:", even, "odd:", odd)
    if len(odd) == 0:
        return "YES"
    elif len(even) != 0:
        return "YES"
    else:
        return "NO"
