def check_dict_case(dict):
    if not dict:
        return False
    # Convert all keys to lower case and remove any keys that are not strings
    lowercase_dict = {str(key).lower(): value for key, value in dict.items() if isinstance(key, str)}
    
    # Convert all keys to upper case and remove any keys that are not strings
    uppercase_dict = {str(key).upper(): value for key, value in dict.items() if isinstance(key, str)}
    
    return lowercase_dict == uppercase_dict