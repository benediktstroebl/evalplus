import re
def valid_date(date):
    """
    Validate a date string and return True if the date is valid, otherwise False.
    """
    # Define a regex pattern to match the date format
    date_pattern = r"^(\d{2})[-/](\d{2})[-/](\d{4})$"

    # Check if the date string matches the pattern
    if re.match(date_pattern, date) is not None:
        # Split the date string into its components
        date_components = list(map(int, re.match(date_pattern, date).groups()))
        # Check the conditions
        if date_components[0] >= 1 and date_components[0] <= 12:
            if date_components[0] % 2 == 0:
                if date_components[1] >= 1 and date_components[1] <= 29:
                    return True
                else:
                    return False
            else:
                if date_components[1] >= 1 and date_components[1] <= 31:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False