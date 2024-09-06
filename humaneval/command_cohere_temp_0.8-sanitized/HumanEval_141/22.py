def file_name_check(file_name):
    regex = r'\b[a-zA-Z][a-zA-Z0-9]{1,2}(\.\w{2})?$'
    if not re.match(regex, file_name):
        return "No"
    else:
        return "Yes"