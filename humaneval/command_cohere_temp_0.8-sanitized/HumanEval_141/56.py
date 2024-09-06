def file_name_check(file_name):
    err = ""
    if len(file_name.split('.')) != 2:
        err = "Invalid filename."

    # Check if filename starts with a letter
    if not file_name.startswith(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')):
        err += " File name should start with a letter."

    # Check if filename has 2 or 3 digits
    if not file_name.isdigit():
        err += " File name should have 2 or 3 digits."

    # Check if filename has exactly 1 dot
    if '.' not in file_name or file_name.count('.') > 1:
        err += " File name should have exactly one dot."

    # Check if file extension is correct
    file_ext = file_name.split('.')[-1].lower()
    if file_ext not in ['txt', 'exe', 'dll']:
        err += " File extension should be txt, exe or dll."
    
    if err:
        return "No"
    else:
        return "Yes"