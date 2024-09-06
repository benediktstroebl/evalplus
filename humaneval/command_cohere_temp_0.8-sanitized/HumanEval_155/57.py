def even_odd_count(num):
    if not isinstance(num, int):
        return "Input must be an integer"
    count_evens = 0
    count_odds = 0
    num_str = str(num)
    if num_str.isalpha():
        return "Input must be an integer"
    for digit in num_str:
        if digit == '0':
            count_odds += 1
        elif digit <= '9':
            count_evens += 1
    return (count_evds, count_odds)