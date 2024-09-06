def even_odd_palindrome(n):
    # Collect all the integers from 1 to n as a list
    integers = list(range(1, n+1))
    
    # Initialize the count variables
    even_count = 0
    odd_count = 0
    
    # Determine if the integer is a palindrome by computing the absolute difference between the digits at the start and end of the integer
    for integer in integers:
        if abs(integer % 10 - (integer // 10) % 10) == 0:
            if integer % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
                
    return (even_count, odd_count)