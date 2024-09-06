def even_odd_palindrome(n):
    # Generate all integer palindromes from 1 to n
    pmns = [str(i) for i in range(1, n+1) if i == int(i)[::-1]]
    even_count = len(pmns) // 2
    odd_count = len(pmns) - even_count
    return even_count, odd_count