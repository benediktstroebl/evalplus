

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Use a dictionary to map each number to the number of times the digit 7 appears in it
    digits = {7: 1, 11: 1, 13: 1, 3: 2, 9: 2, 19: 1, 23: 1, 4: 4, 6: 6, 10: 10, 14: 14, 16: 16, 8: 8, 12: 12, 15: 15, 18: 18, 20: 20, 17: 17, 1: 0, 2: 2, 5: 5, 24: 24, 22: 22, 25: 25, 21: 21, 26: 26, 27: 27, 28: 28, 29: 29, 30: 30}
    
    # Loop through the numbers less than n and increment the count for each digit
    for i in range(n):
        count = 0
        while True:
            digit = i % 10
            if digit in digits:
                count += digits[digit]
                break
            i = i // 10
        print(count)
