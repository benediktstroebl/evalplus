def even_odd_palindrome(n):
    # Count even and odd length palindromes
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        reversed_str = str(i)
        reversed_str = reversed_str[::-1]
        
        if len(reversed_str) == 1:
            continue
        elif len(reversed_str) == 2:
            if int(reversed_str) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        else:
            if int(reversed_str) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
                
    return (even_count, odd_count)