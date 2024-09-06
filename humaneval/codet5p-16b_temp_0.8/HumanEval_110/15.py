
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

    
    # Initialize a list that will store the element count for lst1 and lst2
    count_lst1 = []
    count_lst2 = []
    
    # Iterate over lst1 and get a count for each element in lst1
    for i in range(len(lst1)):
        count_lst1.append(lst1.count(lst1[i]))
    
    # Iterate over lst2 and get a count for each element in lst2
    for i in range(len(lst2)):
        count_lst2.append(lst2.count(lst2[i]))
        
    # Sort the count lists in descending order
    count_lst1.sort(reverse=True)
    count_lst2.sort(reverse=True)
    
    # Iterate over the count lists to see if the lst1 and lst2 can be exchanged
    for i in range(len(count_lst1)):
        if count_lst1[i] <= count_lst2
