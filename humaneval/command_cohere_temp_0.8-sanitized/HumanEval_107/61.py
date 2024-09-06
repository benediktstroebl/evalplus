def even_odd_palindrome(n):
    # Count even and odd length palindromes
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        reversed_str = str(i)
        reversed_count = 0
        
        for j in range(len(reversed_str)):
            if reversed_str[j] == reversed_str[0]:
                reversed_count += 1
            else:
                break
        
        if reversed_count == len(reversed_str) or reversed_count == len(reversed_str)/2:
            if reversed_count == len(reversed_str):
                even_count += 1
            else:
                odd_count += 1
    
    return (even_count, odd_count)