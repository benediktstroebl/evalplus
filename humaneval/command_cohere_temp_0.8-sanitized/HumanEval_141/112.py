def file_name_check(file_name):
    malformed = False
    # Check if the file name has more than 3 digits
    if re.search(r'\d{4,}', file_name):
        return "No"
    
    # Check if the file name has exactly one dot '.'