def count_palindromes(n):
    # memoization for counting even palindromes
    even = [0] * (n + 1)
    even[0] = 1
    even[1] = 0
    for i in range(2, n + 1):
        if i == int(i[0] + i[i - 1]):
            even[i] = even[i - 1] + 1
        else:
            even[i] = even[i - 1]
    # counting odd palindromes
    odd = [0] * (n + 1)
    for i in range(1, n + 1):
        if i == int(i[0] + i[i - 1]):
            odd[i] = odd[i - 1] + 1
        else:
            odd[i] = odd[i - 1] + 1
    return even[n], odd[n]
def even_odd_palindrome(n):
    return count_palindromes(n)