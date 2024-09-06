def even_odd_palindrome(n):
    # Count even and odd length palindromes
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        s = str(i)
        if s == s[::-1] and len(s) % 2 == 0:
            even_count += 1
        elif s == s[::-1] and len(s) % 2:
            odd_count += 1
    
    return (even_count, odd_count)