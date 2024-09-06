def file_name_check(file_name):
    checker = ['1234567890', '.', 'a', 'txt', 'exe', 'dll']
    count = ('0123456789'.count(file_name))
    has_dot = ('.' in file_name)
    pre, post = file_name.split('.')
    alpha = (len(set(pre)) == 1 and pre[0].isalpha())
    ext = (post in checker)
    if count <= 3 and has_dot and alpha and ext:
        return "Yes"
    else:
        return "No"