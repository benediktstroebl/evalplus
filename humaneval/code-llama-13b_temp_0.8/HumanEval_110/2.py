
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

    # Initialize a list of even numbers
    even_nums = []

    # Store the even numbers
    for num in lst1:
        if num % 2 == 0:
            even_nums.append(num)

    # Iterate over lst2 and count the number of occurences of each number in even_nums
    num_count = {}
    for num in lst2:
        if num in even_nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1

    # Check if all the even numbers in lst1 has at least 1 occurence in lst2
    for num in even_nums:
        if num not in num_count:
            return "NO"

    # Return "YES"
    return "YES"









