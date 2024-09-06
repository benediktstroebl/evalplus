def check_dict_case(dict):
    if not dict:
        return False
    # convert keys to lower case and remove non string keys
    lower_case_dict = {key: val for key, val in dict.items() if key and isinstance(key, str)}
    # check if the dictionary is now empty, true if empty
    if not lower_case_dict:
        return True
    # check if the lower case dictionary is equal to the original dictionary
    return lower_case_dict == dict