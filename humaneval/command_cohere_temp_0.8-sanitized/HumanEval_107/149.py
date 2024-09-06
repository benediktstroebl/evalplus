def even_odd_palindrome(n):
    s = str(n)
    count_odd = 0
    count_even = 0
    
    for i in range(1, n + 1):
        if s == str(i) or s == str(n - i + 1):
            if i % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    
    return (count_even, count_odd)