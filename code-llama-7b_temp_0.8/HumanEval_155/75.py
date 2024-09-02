
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Your code here

    even_counter = 0
    odd_counter = 0

    num_string = str(num)

    for i in num_string:
        if int(i) % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1

    return (even_counter, odd_counter)

    # antoher way:
    return tuple(sum(int(i) % 2 == j for i in str(num)) for j in (0, 1))
