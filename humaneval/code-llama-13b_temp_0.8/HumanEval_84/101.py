
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
    # Created by Shubham Diwan
    # https://www.geeksforgeeks.org/find-sum-of-digits-of-a-number-in-binary-representation/
    # and https://www.geeksforgeeks.org/how-to-convert-a-decimal-number-to-binary-in-python/
    # @Author: your name goes here
    # @Date: 2019-10-15 11:49:54
    # @Last Modified by: Shubham Diwan
    # @Last Modified time: 2019-10-15 12:12:10
    def decimalToBinary(n): 
        return bin(n).replace("0b", "") 

    def sumofBinary(n): 
        b = decimalToBinary(n) 
        sum = 0
        for i in b: 
            sum = sum + int(i) 
        return sum
    return sumofBinary(N)
    
