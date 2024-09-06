def even_odd_palindrome(n):
    # Create a counter to track even and odd palindromes
    even, odd = 0, 0
    
    # Loop through numbers from 1 to n and check for palindromes
    for i in range(1, n + 1):
        s = str(i)
        if s == s[::-1]:
            if len(s) % 2 == 0:
                even += 1
            else:
                odd += 1

    return (even, odd)