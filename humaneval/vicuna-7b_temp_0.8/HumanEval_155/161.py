
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # pattern to check if a number is even or odd
    pattern = r"\d\d?"
    # convert the input string to a list of integers
    digits = [int(digit) for digit in str(num)]
    # initialize the count of even and odd digits
    even_count = 0
    odd_count = 0
    # iterate through the digits
    for i in range(len(digits)):
        # check if the current digit is even or odd
        digit = digits[i]
        if digit in "0123456789":
            # if the current digit is a number, increment the count of even and odd digits
            if pattern.search(str(digit)):
                even_count += 1
            odd_count += 1
        else:
            # if the current digit is a non-number, increment the count of odd digits
            odd_count += 1
    return (even_count, odd_count)
