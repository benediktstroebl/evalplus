def check_dict_case(dict):
    if not dict:
        return False
    
    # Convert dictionary keys to lowercase
    lowercase_dict = {key.lower(): value for key, value in dict.items()}
    
    # Convert dictionary keys to uppercase
    uppercase_dict = {key.upper(): value for key, value in dict.items()}
    
    return lowercase_dict == uppercase_dict