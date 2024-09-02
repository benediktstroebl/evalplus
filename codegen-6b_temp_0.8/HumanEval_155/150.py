
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count_odd = 0
    count_even = 0
    # Convert num into a string and find the length of the string
    num_string = str(num)
    num_length = len(num_string)
    # Loop through the string
    for i in range(num_length):
        # Check if the i'th character in the string is an '1' or '0'
        if num_string[i]=='0' or num_string[i]=='1':
            # If the character is either an '1' or '0', increment the count for that character.
            if num_string[i]=='0':
                count_even = count_even + 1
            else:
                count_odd = count_odd + 1
    # Return a tuple that has the number of even and odd digits respectively
    return (count_even, count_odd)
