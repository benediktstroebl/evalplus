def even_odd_palindrome(n):
    # Count even and odd length palindromes
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        # Calculate the length of the reversed integer
        reversed_len = len(str(i))
        
        # Check if the integer is a palindrome
        if i == int(i[::-1]):
            if reversed_len % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    return (even_count, odd_count)