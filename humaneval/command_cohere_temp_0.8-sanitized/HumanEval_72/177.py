def will_it_fly(q, w):
    return (sum(q) <= w) and (w >= max(q)) and palindrome(q)
def palindrome(q):
    return q == q[::-1]