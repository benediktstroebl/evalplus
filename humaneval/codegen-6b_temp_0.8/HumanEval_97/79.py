
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    if a == 0 or b == 0:
        return 0
    # print(a * b)
    if a < 0:
        a = abs(a)
        b = 0-b
    A = []
    while a != 0:
        A.append(a % 10)
        a //= 10
    B = []
    while b != 0:
        B.append(b % 10)
        b //= 10
    count = 0
    for i in range(len(A)):
        if len(B) < i + 1:
            break
        for j in range(len(B) - i):
            if len(A) < j + 1:
                break
            temp = A[j] * B[i+j]
            if count < temp:
                count = temp
    return count

