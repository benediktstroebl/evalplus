def even_odd_palindrome(n):
    # Calculate the maximum number of palindromes
    max_palindromes = n * (n + 1) // 2

    # Count even and odd palindromes
    even_count = 0
    odd_count = 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
    return (even_count, odd_count)