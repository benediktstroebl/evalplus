
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    # Write your code here
    n = str(num)
    num_of_even = 0
    num_of_odd = 0

    for i in n:
        if i % 2 == 0:
            num_of_even += 1
        else:
            num_of_odd += 1

    return num_of_even, num_of_odd

