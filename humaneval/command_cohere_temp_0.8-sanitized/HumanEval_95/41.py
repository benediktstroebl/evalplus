def check_dict_case(dict):
    if not dict:
        return False
    # Convert dictionary keys to lowercase and remove any keys that do not match the original keys to not affect the dict ordering.
    lowercase_dict = {key: dict[key] for key in dict}
    lowercase_dict = {key: lowercase_dict[key] for key in lowercase_dict if key in dict}
    
    # Convert dictionary keys to uppercase and remove any keys that do not match the original keys to not affect the dict ordering.
    uppercase_dict = {key: dict[key] for key in dict}
    uppercase_dict = {key: uppercase_dict[key] for key in uppercase_dict if key in dict}
    
    if set(dict.keys()) == set(lowercase_dict.keys()) or set(dict.keys()) == set(uppercase_dict.keys()):
        return True
    else:
        return False