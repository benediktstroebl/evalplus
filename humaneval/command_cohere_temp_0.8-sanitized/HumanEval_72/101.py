def will_it_fly(q, w):
    return (sum(q) <= w) and check_palindrome(q)
def check_palindrome(q):
    return q == q[::-1]