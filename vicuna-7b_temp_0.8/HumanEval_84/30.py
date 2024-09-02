
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
    # Binary representation of N
    binary = str(N)
    # A variable to store the running sum of digits
    running_sum = ""
    # Loop through each digit in the binary representation of N
    for i in range(len(binary)):
        # Keep track of the highest power of 2 at which N is divisible
        highest_power = 0
        # Loop through each digit in the binary representation of N
        for j in range(len(binary)):
            # If the binary representation of N ends in 0, the next digit is the highest power of 2 at which N is divisible
            if binary[j] == "0":
                next_digit = 2 ** highest_power
            # If the binary representation of N ends in 1, the next digit is the highest power of 2 at which N is divisible
            else:
                next_digit = 2 ** highest_power + 1
            # Calculate the sum of digits from the current position in the binary representation to the next digit
            sum = sum(map(int, binary[j:].split()))
            # Update the running sum
            running_sum += sum // next_digit
            # Update the highest power of 2
            highest_power = sum % next_digit
    return running_sum
