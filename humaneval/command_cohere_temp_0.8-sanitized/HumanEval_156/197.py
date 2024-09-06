def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")

    # Convert number to list of digits and reverse it
    digits = list(str(n))[::-1]
    result = []

    for i in range(len(digits)):
        # Convert current digit to roman numeral
        digit = digits[i]
        if digit == '1':
            result.append('i')
        elif digit == '2':
            result.append('ii')
        elif digit == '3':
            result.append('iii')
        elif digit == '4':
            result.append('iv')
        elif digit == '5':
            result.append('v')
        elif digit == '6':
            result.append('vi')
        elif digit == '7':
            result.append('vii')
        elif digit == '8':
            result.append('viii')
        elif digit == '9':
            result.append('ix')
        elif digit == '0':
            result.append('x')

    # Join roman numerals to form the final result
    return ''.join(result)