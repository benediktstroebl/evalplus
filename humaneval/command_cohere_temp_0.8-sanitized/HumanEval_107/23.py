def even_odd_palindrome(n):
    even, odd = 0, 0
    for num in range(1, n+1):
        if str(num) == str(num)[::-1]:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)