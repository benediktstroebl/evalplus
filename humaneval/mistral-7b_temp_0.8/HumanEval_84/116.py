
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
    # Write your code here
    import math

    def bin(number):
        n = int(math.log(number, 2) + 1)
        result = []
        while number > 0:
            result.append(number % 2)
            number = number // 2
        result.reverse()
        return result

    def sum_binary(number):
        result = 0
        for i in number:
            result += i
        return result

    def to_str(number):
        result = ""
        for i in number:
            result += str(i)
        return result

    def get_digits_sum(number):
        return to_str(sum_binary(bin(number)))
    return get_digits_sum(N)

