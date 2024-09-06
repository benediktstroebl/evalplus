

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    if n > 100:
        return 0
    
    for i in range(1, n):
        if i % 11 == 0:
            # if the number is divisible by 11, add the string 'Fizz'
            output = 'Fizz'
        elif i % 13 == 0:
            # if the number is divisible by 13, add the string 'Buzz'
            output = 'Buzz'
        elif i % 7 == 0:
            # if the number is divisible by 7, add the string 'Buzz'
            output = 'Buzz'
        else:
            # if the number is divisible by neither 11 nor 13, add the string 'Fizz'
            output = 'Fizz'
        
        # if the number has already been outputted, increment the count
        if output == 'Fizz':
            count += 1
        
        # output the number and the next digit in the output string
        print(i, output)
        output = 'Fizz' if output == 'Fizz' else 'Buzz'
    
    # output the final count
    print(count)
