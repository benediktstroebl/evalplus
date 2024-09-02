
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

    # 생각해보니 입력값이 1000이라고 했을 때 12자리 문자열로 바꿔서 출력하면 되는게 아닌
    # 그냥 2진수로 변환해서 출력하면 될 듯 하다

    # 1. 입력값에서 0, 1로 분리하고 각각의 개수를 세기
    ones, zeros = [], []
    for i in range(N):
        if i % 2 == 0:
            zeros.append(i)
        else:
            ones.append(i)

    # 2. 2진수로 변환해서 출력
    result = ""
    for n in range(len(ones) + len(zeros)):
        if n in ones:
            result += "1"
        else:
            result += "0"

    return result
