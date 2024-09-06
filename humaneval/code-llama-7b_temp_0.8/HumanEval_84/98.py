
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
    #Binary convert
    s=str(bin(N))
    #the length of the binary number
    l=len(s)
    #if the length is 2, there is no need to slice, so that we can avoid the case of 10.
    if l==3:
        return s[2:]
    else:
        return s[l-2:]
    
    
    """
        #Method 1:
    #Binary convert
    s=str(bin(N))
    #the length of the binary number
    l=len(s)
    #if the length is 2, there is no need to slice, so that we can avoid the case of 10.
    if l==3:
        return s[2:]
    else:
        return s[l-2:]
        
        #Method 2:
        s=str(bin(N))
        l=len(s)
        if l==3:
            return s[2:]
        else:
            return s[l-2:]
        #A better Method:
        return str(bin(N))[-1:]
    """
    
