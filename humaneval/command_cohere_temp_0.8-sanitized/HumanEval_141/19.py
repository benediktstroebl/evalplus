def file_name_check(file_name):
    txt_dll_exe = ['txt', 'dll', 'exe']
    
    # Check if string contains more than 3 digits
    if len(set(char for char in file_name if char.isdigit())) > 3:
        return "No"
    
    # Check if the file name contains exactly one dot '.'
    if '.' not in file_name or file_name.count('.') > 1:
        return "No"
    
    # Check if the substring before the dot starts with a letter
    if not file_name.count('.') and not file_name.startswith(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')):
        return "No"
    
    # Check if the substring after the dot is in txt_dll_exe
    if not file_name.count('.') and file_name.split('.')[-1].lower() not in txt_dll_exe:
        return "No"
    
    return "Yes"