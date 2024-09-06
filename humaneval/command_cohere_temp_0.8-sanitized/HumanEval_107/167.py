def even_odd_palindrome(n):
    # Initialize counts for even and odd palindromes
    even_count = 0
    odd_count = 0
    
    # Utilize a generator expression to detect palindromes
    for num in range(1, n + 1):
        if str(num) == str(num)[::-1]:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)