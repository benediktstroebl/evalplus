def even_odd_palindrome(n):
    # Count even and odd length palindromes
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        reversed_str = str(i)
        reversed_count = 0
        
        for j in range(1, len(reversed_str)+1):
            if reversed_str[:j] == reversed_str[::-1]:
                reversed_count += 1
        
        if reversed_count == 2:
            even_count += 1
        elif reversed_count == 1:
            odd_count += 1
    
    return (even_count, odd_count)