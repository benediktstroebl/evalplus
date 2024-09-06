
def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    # Goal: Return a string of binary numbers

    # What is the result that we need to calculate?
    # The total sum of the digits in binary
    # To get this, we need to convert N to binary, then add up the digits
    #
    # Create a variable to store the result
    total_sum = 0

    # Convert N to binary
    bin_n = bin(N)
    print(f"bin_n = {bin_n}")
    # The output will be something like "0b10010", where the "0b" is just a prefix,
    # and the rest are the digits.
    # We need to get rid of the prefix and only work with the digits
    # To do that, we use the .replace() string method
    # The input will be "0b10010", and the output will be "10010"
    bin_n = bin_n.replace("0b", "")
    print(f"bin_n = {bin_n}")
    # Now that the prefix is gone, we need to convert the string of digits to
    # a list so that we can work with them as numbers
    bin_n = list(bin_n)
    print(f"bin_n = {bin_n}")

    # Get the sum of the digits
    # We will do this by converting each number in the list to an integer, and
    # then adding them together
    # Loop through each number
    for num in bin_n:
        # Convert the number to an integer
        num = int(num)
        # Add it to the total
        total_sum += num

    # Print the result
    # Now that we have the sum, we need to convert it to binary
    # We can use the bin() function to do that
    # bin(total_sum) will give us the binary number of total_sum
    # We need to get rid of the prefix "0b" and just work with the digits
    # so we can do that with .replace("0b", "")
    # We also need to convert this to a string, since our goal is to return
    # a string of digits, not a number
    bin_total
