
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    # 주석 처리된 코드는 오류를 발생시키는 코드입니다.
    # n = 235
    n = int(input())
    # 리스트에 각 자릿수를 저장합니다.
    digits = [int(digit) for digit in str(n)]
    # 홀수 자릿수만 곱하기
    result = 1
    for digit in digits:
        if digit % 2 != 0:
            result *= digit
    return result

