
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
    def file_name_checker(file_name):
        error_dict = {'0':"The file name should not have more than three digits ('0'-'9').",
                      '1':"The file name should contain exactly one dot '.'.",
                      '2':"The substring before the dot should not be empty, and it starts with a letter from the latin alphapet ('a'-'z' and 'A'-'Z').",
                      '3':"The substring after the dot should be one of these: ['txt', 'exe', 'dll']"}
        
        status = 'Yes'
        if len(file_name.strip()) == 0:
            status = 'No'
        elif file_name[0] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            status = 'No'
        elif file_name.count(".") != 1:
            status = 'No'
        elif file_name[-3:] not in ['txt', 'exe', 'dll']:
            status = 'No'
                
        return status
    return file_name_checker
                
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    