def check_dict_case(dict):
    if not dict:
        return False
    # Convert dictionary keys to lowercase and remove any keys that do not match the original set of keys
    lower_case_dict = {key: val for key, val in dict.items()}
    lower_case_dict = {key: val for key, val in lower_case_dict.items() if key in dict}
    
    # Convert dictionary keys to uppercase and remove any keys that do not match the original set of keys
    upper_case_dict = {key: val for key, val in dict.items()}
    upper_case_dict = {key: val for key, val in upper_case_dict.items() if key in dict}
    
    if len(lower_case_dict) == len(upper_case_dict):
        return True
    return False