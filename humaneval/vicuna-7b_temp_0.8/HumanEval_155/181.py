
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # check if num is negative
    if num < 0:
        return (-1, -1)

    # check if num is a single digit number
    if len(str(num)) == 1:
        return (1 if str(num)[-1] == '1' else 0, 0)

    # convert num to a string
    num_str = str(num)

    # initialize even and odd counts
    even = 0
    odd = 0

    # iterate through each digit in the string
    for i in range(len(num_str)):
        # check if the current digit is even
        if num_str[i] in '01':
            # if the current digit is even, increment even count
            even += 1
        else:
            # if the current digit is odd, increment odd count
            odd += 1

    # return the counts
    return (even//2, odd//2) if even % 2 == 0 else (even//2+1, odd//2+1)
