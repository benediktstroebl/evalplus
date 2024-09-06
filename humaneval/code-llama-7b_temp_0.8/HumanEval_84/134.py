
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
    #
    # You code here
    #

    #number = N
    #binary_list = []
    # while number >= 1:
    #     remainder = number % 2
    #     binary_list.append(str(remainder))
    #     number = number // 2
    #
    # return "".join(binary_list)

    #open dictionary
    dict = {0 : "0", 1 : "1"}
    #make binary
    result = ""
    while N != 0:
        remainder = N % 2
        result += dict[remainder]
        N = N // 2
    return result[::-1]
    # return result
