def file_name_check(file_name):
    checker = lambda s: len(s) <= 1 and s[0] in '.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    num_digits = sum(1 for c in file_name if c in '0123456789')
    has_dot = '.' in file_name
    substring_before_dot, file_extension = file_name.split('.')[:2]
    
    passes_letter_check = checker(substring_before_dot) and checker(file_extension)
    
    valid_extensions = ['txt', 'exe', 'dll']
    passes_extension_check = file_extension in valid_extensions
    
    if num_digits <= 1 and has_dot and passes_letter_check and passes_extension_check:
        return "Yes"
    else:
        return "No"