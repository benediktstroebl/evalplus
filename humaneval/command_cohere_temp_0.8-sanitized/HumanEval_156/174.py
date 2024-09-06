def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")

    # Convert number to list of digits and reverse it to iterate backwards
    digits = list(reversed(str(n)))
    
    result = []
    
    for i in range(len(digits)):
        # Extract the specific digit and count it as cumulative total
        digit = digits[i]
        total = sum(digits[:i+1])

        # Special case for singles
        if i == 0 and digit == '1':
            result.append(digit)
        elif digit == '1':
            result.append(f'{total}x')
        # Special case for fives
        elif i == 0 and digit == '5':
            result.append('v')
        elif digit == '5':
            result.append(f'{total}x')
        # All other cases
        else:
            result.extend(mini_roman_map[digit] for digit in digits[:i+1])

    return ''.join(result)
mini_roman_map = {
    '0': 'nul',
    '1': 'x',
    '2': 'ii',
    '3': 'iii',
    '4': 'iv',
    '5': 'v',
    '6': 'vi',
    '7': 'vii',
    '8': 'viii',
    '9': 'ix',
    '10': 'x'
}