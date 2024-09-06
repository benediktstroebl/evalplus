def file_name_check(file_name):
    fo = []
    d = dict()
    n = file_name.split('.')
    if len(n) == 2:
        if n[0].isalpha() and n[0].strip() != '':
            s = n[0]
        else:
            return 'No'
        if len(n[1]) == 3 and n[1].isdigit():
            t = n[1]
        else:
            return 'No'
        if t in d:
            fo.append(d[t])
        else:
            d[t] = len(fo)
            fo.append(t)
        if len(fo) <= 3 and s + '.' + t == file_name:
            return 'Yes'
    return 'No'