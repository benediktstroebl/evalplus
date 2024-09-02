
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
    # 
    # # Solution with PyParsing
    # integer = Combine(Optional(oneOf("+ -")) + Word(nums))
    # dot = Literal(".")
    # before_dot = Combine(Word(alphas + "_") + Optional(integer))
    # after_dot = oneOf("txt exe dll")
    # # Create the grammar
    # filename_check = before_dot + dot + after_dot
    # # Evaluate the grammar
    # try:
    #     if len(filename_check.parseString(file_name, parseAll=True)) == 1:
    #         return "Yes"
    #     else:
    #         return "No"
    # except ParseException:
    #     return "No"
    # 
    # Solution with regular expressions
    regex = "([a-zA-Z]+\d?[a-zA-Z]*|[a-zA-Z]+)\.(txt|exe|dll)"
    if re.match(regex, file_name):
        return "Yes"
    else:
        return "No"

