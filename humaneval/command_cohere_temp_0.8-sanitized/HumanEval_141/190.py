def file_name_check(file_name):
    checker = lambda s: len(s) > 0 and s[0].isalpha() and s.count('.') == 1 and \
                       sum(c.isdigit() for c in s) <= 3 and \
                       (s.split('.')[-1] in ['txt', 'exe', 'dll'] or s.split('.')[-2] in ['txt', 'exe', 'dll'])
    return 'Yes' if checker(file_name) else 'No'