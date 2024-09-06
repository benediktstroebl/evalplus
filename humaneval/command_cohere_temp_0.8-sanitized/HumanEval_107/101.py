def even_odd_palindrome(n):
    # collect all positive integer palindromes and categorize them based on parity
    count_odd = 0
    count_even = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)