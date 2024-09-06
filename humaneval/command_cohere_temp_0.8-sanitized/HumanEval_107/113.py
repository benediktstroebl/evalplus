def count_palindromes(n):
    s = str(n)
    ev = se = 0
    for e in s:
        if e == e[::-1]:
            ev += 1
        else:
            se += 1
    return ev, se
def even_odd_palindrome(n):
    return count_palindromes(n)