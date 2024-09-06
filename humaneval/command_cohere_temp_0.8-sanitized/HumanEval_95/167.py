def check_dict_case(dict):
    if not dict:
        return False
    # Convert dictionary keys to lowercase and remove any keys that are not strings
    lowercase_dict = {key: value for key, value in dict.items() if isinstance(key, str)}
    all_keys_lower = all(key in lowercase_dict for key in lowercase_dict.keys())
    # Convert dictionary keys to uppercase and remove any keys that are not strings
    uppercase_dict = {key: value for key, value in dict.items() if isinstance(key, str)}
    all_keys_upper = all(key in uppercase_dict for key in uppercase_dict.keys())
    return all_keys_lower or all_keys_upper