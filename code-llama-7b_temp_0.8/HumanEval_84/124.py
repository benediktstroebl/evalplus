
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
    # a: is a base ten integer
    a = N
    # b: is the binary representation of a
    b = ''
    # c: is the sum of the digits in b
    c = ''
    # if a is equal to zero then
    if a == 0:
        # c should be the number "0"
        c = '0'
        # return c
        return c
    # else
    else:
        # while a is greater than zero
        while a > 0:
            # remainder of a divided by two
            x = a % 2
            # divide a by two
            a = a // 2
            # append remainder to the end of b
            b = b + str(x)
        # set c to the string representation of the sum of the digits in b
        c = str(sum(int(x) for x in b))
        # return c
        return c
