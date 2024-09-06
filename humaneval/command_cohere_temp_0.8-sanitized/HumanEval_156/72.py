def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")

    # Convert number to list of digits and reverse it to avoid incorrect leading values
    digits = [int(d) for d in str(n)[::-1]]
    
    result = []
    for i in range(len(digits)):
        digit = digits[i]
        if digit < 5: 
            result.append(str(digit))
        else:
            result.append('x')
            digit -= 5
            result.append(chr(ord('a') + digit))
            
    return ''.join(result).lower()