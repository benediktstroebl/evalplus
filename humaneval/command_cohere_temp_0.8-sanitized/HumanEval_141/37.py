def file_name_check(file_name):
    checks = []
    
    # Check if there's more than three digits in the filename
    digits = '[0-9]{4,}'
    if re.search(digits, file_name):
        return 'No'
    
    # Check for exactly one dot in the filename