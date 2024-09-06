
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    def is_valid_file_name(file_name):
        """
        Returns 'Yes' if the file name is valid, and 'No' otherwise.
        """
        # use regex to check if there are more than 3 digits in the file's name 
        regex = "^[a-zA-Z_][a-zA-Z0-9_.]*"
        if re.match(regex, file_name):
            # substring before the dot
            frst_substr = file_name[:file_name.rfind(".")]
            # if the first substring is not empty and starts with a lienar alphapet
            if frst_substr and re.match("^[a-zA-Z_][a-zA-Z0-9_.]*$", frst_substr):
                # substring after the dot
                sec_substr = file_name[file_name.rfind(".") + 1:]
                # substring after the dot must be one of these
                sec_substr_list = ["txt", "exe", "dll"]
                if sec_substr and sec_substr in sec_substr_list:
                    return "Yes"
                else:
                    return "No"
            else:
                return "No"
        else:
            return "No"
    return is_valid_file_name

