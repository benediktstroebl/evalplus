
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
    results = [0]
    d = 0
    while True:
        if results[-1] < 2**N - 1:
            results.append(results[-1] + 2**N)
        else:
            break
    
    results = [str(bin(x))[2:] for x in results]
    results = "".join(results)[::-1]
    return results

