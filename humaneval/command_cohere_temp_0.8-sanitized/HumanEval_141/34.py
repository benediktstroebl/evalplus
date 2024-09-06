def file_name_check(file_name):
    assert not any(char in file_name for char in '0123456789'), "There should not be more than three digits ('0'-'9') in the file's name"
    assert '.' in file_name, "The file's name contains exactly one dot '.'"
    assert file_name[:file_name.index('.')].isalpha(), "The substring before the dot should not be empty, and it starts with a letter from the latin alphapet ('a'-'z' and 'A'-'Z')"
    assert file_name[-3:].lower() in ['txt', 'exe', 'dll'], "The substring after the dot should be one of these: ['txt', 'exe', 'dll']"
    
    if not any(char in file_name for char in '0123456789') and '.' in file_name and file_name[:file_name.index('.')].isalpha() and file_name[-3:].lower() in ['txt', 'exe', 'dll']:
        return "Yes"
    else:
        return "No"