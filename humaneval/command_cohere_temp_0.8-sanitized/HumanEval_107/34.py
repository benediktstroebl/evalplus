def even_odd_palindrome(n):
    # collect all positive integer palindromes and categorize them based on parity
    counts = collections.Counter(str(i) for i in range(1, n+1) if i == int(str(i)[::-1]))
    even, odd = 0, 0
    for num in counts:
        if counts[num] % 2 == 0:
            even += counts[num]
        else:
            odd += counts[num]
    return (even, odd)