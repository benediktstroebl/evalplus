def file_name_check(file_name):
    lambda_string = lambda s: len(s) <= 3 and s.isalpha() and s[:1].isalpha() and s[-1] == '.'
    lambda_func = lambda s, l: s == '.' or (l == 'txt' or l == 'exe' or l == 'dll')
    if lambda_string(file_name) and lambda_func(file_name[1:], file_name[3:]):
        return "Yes"
    else:
        return "No"