def even_odd_palindrome(n):
    even, odd = 0, 0
    for num in range(1, n+1):
        reversed_num = str(num)
        if reversed_num == reversed_num[::-1] and int(reversed_num) == num:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)