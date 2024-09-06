
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

    num1 = a
    num2 = b
    
    # Get last digit
    last_digit1 = num1 % 10
    last_digit2 = num2 % 10

    # get remaining number without last digit
    num1 = num1 // 10
    num2 = num2 // 10

    # get the sum
    last_digit_sum = last_digit1 * last_digit2

    # get the final answer
    return (last_digit_sum + multiply(num1, num2))
