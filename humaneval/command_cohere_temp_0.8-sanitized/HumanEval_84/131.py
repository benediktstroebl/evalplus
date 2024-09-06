def solve(N):
    # Convert the integer to a string
    N_str = str(N)
    sum_list = []
    
    # Get the length of the integer
    l = len(N_str)
    
    # Loop through the digits and add them in reverse to the sum list
    for i in range(l):
        dig = N_str[i]
        dig_bin = bin(int(dig))[2:]
        if dig_bin:
            sum_list.append(dig_bin)
    # Convert the list of binary digits to a string and add to the result
    result = ''.join(reversed(sum_list))
    return result