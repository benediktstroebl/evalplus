def check_dict_case(dict):
    if not dict:
        return False
    # Convert all keys to lowercase for comparison
    lowercase_dict = {key.lower(): value for key, value in dict.items()}
    # Convert all keys to uppercase for comparison
    uppercase_dict = {key.upper(): value for key, value in dict.items()}
    return (lowercase_dict == uppercase_dict) and all([isinstance(key, str) for key in dict])