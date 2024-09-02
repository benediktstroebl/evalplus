
def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    #print "solve:", s
    s = s.lower()
    if '#' in s:
        s = s[:s.find('#')]
    s = s.replace('#', '%').replace('@', '#').replace('%', '@')
    s = re.sub(r'\W', '', s)
    if len(s) != 0:
        s = s[::-1]
    return s

tests = [
    ('1234', '4321'),
    ('ab', 'AB'),
    ('#a@C', '#A@c'),
    ('abc', 'abc'),
    ('', ''),
    ('ab#', 'ba#'),
    ('x', 'x'),
    ('ab', 'ab'),
    ('#a@C', '#A@c'),
    ('##', '#'),
    ('##', '#'),
    ('##', ''),
]

for i, (s, expected) in enumerate(tests, 1):
    res = solve(s)
    if res != expected:
        print(f'Test {i} - fail, got {res} for s={s} but expected {expected}')
    else:
        print(f'Test {i}: OK')
