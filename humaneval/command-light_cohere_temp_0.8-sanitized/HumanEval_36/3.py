def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Convert n to a list of digits
    digits_n = list(str(n))
    # Remove non-digit characters
    digits_n = [c for c in digits_n if c.isdigit()]
    
    count = 0
    for num in range(10**n, 0, -1):
        # Convert num to a list of digits
        num_digits = list(str(num))
        # Remove non-digit characters
        num_digits = [c for c in num_digits if c.isdigit()]
       
            # Find the number in num_digits whose digit is 7
        for i in range(len(num_digits)):
            if num_digits[i] == '7':
                count += 1
        # Add count for the number
        num_str = str(num)
        count_str = '{}'.format(count)
        # Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13
        return count_str