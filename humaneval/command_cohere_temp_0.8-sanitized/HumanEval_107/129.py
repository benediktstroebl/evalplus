def even_odd_palindrome(n):
    # Count even and odd length palindromes
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        reversed_str = str(i)
        reversed_len = len(reversed_str)
        
        if reversed_len == 1:
            continue
        elif reversed_len % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return (even_count, odd_count)