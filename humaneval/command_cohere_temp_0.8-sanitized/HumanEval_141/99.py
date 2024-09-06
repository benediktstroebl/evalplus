def file_name_check(file_name):
    import re

    pattern = r'\b[a-zA-Z][a-zA-Z0-9]{1,2}(\.\w{2})?\b(?:\.txt|\.exe|\.dll)'
    
    if re.search(pattern, file_name):
        return "Yes"
    else: 
        return "No"