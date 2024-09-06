def generate_palindromes(n):
    odd = 0
    even = 0
    for i in range(1, n+1):
        reversed_str = str(i)
        reversed_str = reversed_str[::-1]
        if int(reversed_str) == i:
            if len(reversed_str) % 2 == 0:
                even += 1
            else:
                odd += 1
    return even, odd
def even_odd_palindrome(n):
    even, odd = generate_palindromes(n)
    return (even, odd)