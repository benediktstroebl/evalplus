def check_dict_case(dict):
    if not dict:
        return False
    # Convert dictionary keys to lowercase
    lower_case_dict = {key.lower(): value for key, value in dict.items()}
    # Convert dictionary keys to uppercase
    upper_case_dict = {key.upper(): value for key, value in dict.items()}
    # Check if all keys are the same case
    if lower_case_dict == upper_case_dict or dict == upper_case_dict:
        return True
    else:
        return False