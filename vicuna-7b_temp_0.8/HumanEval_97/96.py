
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
    # base case: if the length of the strings is less than 10, the product is 1
    if len(str(a)) + len(str(b)) < 10:
        return str(a) + str(b)

    # divide the strings by 10 and take the unit digits
    left = str(a)[-1]
    right = str(b)[-1]
    unit_a = str(a // 10)[:-1]
    unit_b = str(b // 10)[:-1]

    # check the digit pairs
    if left in (unit_b, unit_a) and right in (unit_b, unit_a):
        # this happens when the result is 0
        return "0"
    elif (unit_a in (unit_b, unit_a) and left == right) or (unit_b in (unit_a, unit_b) and left == right):
        # this happens when the result is 0
        return "0"

    # compute the final result
    result = str(a) + str(b)

    # subtract the final result from the product of the digits
    # and add the carry to the next iteration
    carry = 0
    for i in range(len(result)):
        digit = result[i]
        if (unit_a in (digit, str(digit)) and left == digit) or (unit_b in (digit, str(digit)) and left == digit):
            carry += 1
        result = str(int(result) + carry) + str(digit)

    # if carry is 1, we need to add 1 to the final result
    if carry == 1:
        result = "1" + result

    return result
