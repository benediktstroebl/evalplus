def file_name_check(file_name):
    fut = []
    if len(file_name) > 0:
        ok = True
        letters = ['a'-'z','A'-'Z']
        # condition 1
        if len(set(file_name)) > 3:
            ok = False
        # condition 2
        if '.' not in file_name:
            ok = False
        else:
            ft = file_name.split('.')
            # condition 3
            if not (ft[0][0] in letters and len(ft[0]) > 0):
                ok = False
            # condition 4
            if ft[1] not in ['txt', 'exe', 'dll']:
                ok = False
        if ok:
            return "Yes"
        else:
            return "No"
    else:
        return "No"