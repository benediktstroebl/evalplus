def even_odd_palindrome(n):
    # Counter for even and odd palindromes
    even, odd = 0, 0
    
    # Range to iterate through numbers up to n
    for num in range(1, n+1):
        # If the number is a palindrome and is even
        if str(num) == str(num)[::-1] and num % 2 == 0:
            even += 1
        # If the number is a palindrome and is odd
        elif str(num) == str(num)[::-1] and num % 2 != 0:
            odd += 1
    
    return (even, odd)