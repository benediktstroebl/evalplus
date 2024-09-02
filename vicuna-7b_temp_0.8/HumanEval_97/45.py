
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
    # use the binary_to_radix function
    # and convert a and b to binary
    a_bin = binary_to_radix(a, 10)
    b_bin = binary_to_radix(b, 10)
    # calculate the sum of the digits
    a_sum = 0
    b_sum = 0
    for i in range(len(a_bin)):
        a_sum += a_bin[i] * (10**len(a_bin)-1)
        b_sum += b_bin[i] * (10**len(b_bin)-1)
    # convert the sum back to decimal
    a_sum = int(a_sum)
    b_sum = int(b_sum)
    # subtract the two sums
    product = a_sum - b_sum
    # convert the product back to decimal
    product = int(product)
    return product