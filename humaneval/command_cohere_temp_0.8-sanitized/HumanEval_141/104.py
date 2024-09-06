def file_name_check(file_name):
    checker = lambda s: len(s) > 0 and s[0].isalpha() and s.count('.') == 1 and \
                   sum(d in s for d in '0123456789') <= 3 and \
                   (s.split('.')[1:] == ['txt', 'exe', 'dll'] or s.split('.')[1:] == [''])
  
    return 'Yes' if checker(file_name) else 'No'