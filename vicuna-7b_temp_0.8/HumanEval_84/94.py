
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
    # variable to store the sum of digits
    d = 0
    # loop through the binary representation of N
    for i in str(N):
        # for digits from 0 to 5
        if i.isdigit():
            d = d * 2 + int(i)
        # for digits from 6 to 9
        elif i.isdigit() and i.isdigit():
            d = d * 2 + int(i) + int(i[1:])
        # for digits 10 to 15
        elif i.isdigit() and i.isdigit() and i.isdigit() and i.isdigit():
            d = d * 2 + int(i) + int(i[1:]) + int(i[2:])
        # for digits 16 to 19
        elif i.isdigit() and i.isdigit() and i.isdigit() and i.isdigit() and i.isdigit() and i.isdigit():
            d = d * 2 + int(i) + int(i[1:]) + int(i[2:]) + int(i[3:])
        # for digits 20 to 21
        elif i.isdigit() and i.isdigit() and i.isdigit() and i.isdigit() and i.isdigit() and i.isdigit() and i.isdigit():
            d = d * 2 + int(i) + int(i[1:]) + int(i[2:]) + int(i[3:]) + int(i[4:])
        # for digits 22 to 23
        elif i.isdigit() and i.isdigit() and i.isdigit() and i.isdigit() and i.isdigit() and i.isdigit() and i.isdigit() and i.isdigit():
            d = d * 2 + int(i) + int(i[1:]) + int(i[2:]) + int(i[3:]) + int(i[4:]) + int(i[5:])
        # for digits 24 to 25
        elif i.isdigit() and i.isdigit() and i.is
