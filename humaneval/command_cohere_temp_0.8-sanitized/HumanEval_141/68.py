def file_name_check(file_name):
    lacticks = 0
    cnt = 0
    tick_present = False
    for char in file_name:
        if char.isdigit():
            cnt += 1
        elif char == '.':
            tick_present = True
        elif char.isalpha():
            lacticks += 1
            cnt = 0
        else:
            pass
    if lacticks > 0 and tick_present and cnt <=3 and file_name.split(".")[1] in ["txt", "exe", "dll"]:
        return "Yes"
    return "No"