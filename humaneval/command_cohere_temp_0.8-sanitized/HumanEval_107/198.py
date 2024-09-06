def even_odd_palindrome(n):
    # Ensure n is a positive integer
    n = abs(n)
    
    # Generate all integer palindromes from 1 to n
    pmns = [str(i) for i in range(1, n + 1)]
    pmns = [p for p in pmns if p == p[::-1]]
    
    # Count even and odd integer palindromes
    even_count = sum(1 for p in pmns if len(p) % 2 == 0)
    odd_count = sum(1 for p in pmns if len(p) % 2 == 1)
    
    return (even_count, odd_count)