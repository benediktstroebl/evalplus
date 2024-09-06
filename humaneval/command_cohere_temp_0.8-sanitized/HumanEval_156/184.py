def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")

    # Convert integer to baseominals & handle special cases
    roman = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = []
    for i in range(len(roman)):
        while n >= roman[i]:
            result.append(str(roman[i]))
            n -= roman[i]

    # Reverse list & join into string
    result.reverse()
    mini_roman = ''.join(result)

    return mini_roman.lower() if mini_roman else None