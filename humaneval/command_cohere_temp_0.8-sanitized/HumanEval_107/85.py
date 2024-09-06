def even_odd_palindrome(n):
    # Record the number of odd and even palindromes
    odd_count = 0
    even_count = 0
    
    # Range of integers to consider (inclusive of 1 and n)
    for num in range(1, n+1):
        # Check if the number is a palindrome
        if str(num) == str(num)[::-1]:
            # If the number is palindrome, check its parity
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    return even_count, odd_count