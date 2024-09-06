
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

    #    dec_to_bin = {
    #        0: "0",
    #        1: "1",
    #        2: "10",
    #        3: "11",
    #        4: "100",
    #        5: "101",
    #        6: "110",
    #        7: "111",
    #        8: "1000",
    #        9: "1001",
    #    }
    #
    #    bin_num = str()
    #
    #    while N:
    #        bin_num += dec_to_bin[N % 10]
    #        N = N // 10
    #
    #    return bin_num[::-1]

    return bin(N)[2:]
