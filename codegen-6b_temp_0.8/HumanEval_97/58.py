
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
    a,b=abs(a),abs(b)

    if a < b:
        a,b=b,a

    res = 0

    while a != 0:
        digit = a % 10
        res = res + digit * b
        a = a // 10

    if res < 0:
        return -1 * res

    return res


n = int(input())
for _ in range(n):
    a,b = [int(x) for x in input().split()]
    print(multiply(a,b))
        
