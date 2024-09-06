
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Use a dictionary to keep track of the number of times each digit appears
    # Initialize the dictionary with zeros
    digit_count = {digit: 0 for digit in '0123456789'}
    # For each digit in the number
    for digit in str(num):
        # Increment the count of the digit in the number
        digit_count[digit] += 1
        # If the digit is odd, increment the count of the next digit
        if digit % 2 == 1:
            digit_count[str(digit + 1)] += 1
    # Return the number of even and odd digits
    return len(digit_count), sum(digit_count.values())