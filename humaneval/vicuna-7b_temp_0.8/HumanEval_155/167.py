
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Convert the number to a string and then to a list
    num_str = str(num)
    num_list = list(num_str)

    # If the number is negative, change the sign
    if num < 0:
        num_list = [-num_list.index(num_list[0]), num_list]

    # Get the total number of digits
    total_digits = len(num_list)

    # Initialize variables for tracking the number of even and odd digits
    even_count = 0
    odd_count = 0

    # Loop through each digit and increment the count of even and odd digits accordingly
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Return the count of even and odd digits
    return (even_count, odd_count)
