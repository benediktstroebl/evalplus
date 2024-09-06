def check_dict_case(dict):
    if not dict:
        return False
    # convert keys to lower case and remove non string keys
    lower_case_dict = {key: val for key, val in dict.items() if key and isinstance(key, str)}
    # convert keys to upper case and remove non string keys
    upper_case_dict = {key: val for key, val in dict.items() if key and isinstance(key, str)}
    upper_case_dict = {key.upper(): val for key, val in upper_case_dict.items()}
    return lower_case_dict == upper_case_dict